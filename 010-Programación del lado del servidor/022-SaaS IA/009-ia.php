<?php
declare(strict_types=1);

/* ================================
   CONFIGURACIÓN
================================ */
$OLLAMA_URL = "http://localhost:11434/api/generate";
$MODEL      = "qwen2.5-coder:7b";

$db_host = "localhost";
$db_user = "saasia";
$db_pass = "SaasIA123$";
$db_name = "saasia";

/* ================================
   FUNCIONES
================================ */

function h($s){
    return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8');
}

function llamarOllama(string $ollamaUrl, string $model, string $prompt, int $timeout = 120): array {
    $data = [
        "model"  => $model,
        "prompt" => $prompt,
        "stream" => false
    ];

    $ch = curl_init($ollamaUrl);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ["Content-Type: application/json"]);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data, JSON_UNESCAPED_UNICODE));
    curl_setopt($ch, CURLOPT_TIMEOUT, $timeout);

    $response = curl_exec($ch);
    if($response === false){
        $err = curl_error($ch);
        curl_close($ch);
        return ["ok" => false, "error" => "Error cURL: ".$err];
    }
    curl_close($ch);

    $result = json_decode($response, true);
    if(!is_array($result)){
        return ["ok" => false, "error" => "Respuesta JSON inválida del modelo."];
    }

    return ["ok" => true, "response" => trim((string)($result["response"] ?? ""))];
}

function ejecutarSQL($sql, $db_host, $db_user, $db_pass, $db_name){
    $mysqli = new mysqli($db_host, $db_user, $db_pass, $db_name);

    if($mysqli->connect_errno){
        return ["error" => "Error conexión DB: ".$mysqli->connect_error];
    }

    $resultado = $mysqli->query($sql);

    if($resultado === false){
        return ["error" => $mysqli->error];
    }

    if($resultado instanceof mysqli_result){
        $filas = [];
        while($row = $resultado->fetch_assoc()){
            $filas[] = $row;
        }
        return ["type" => "select", "data" => $filas];
    }

    return [
        "type"     => "action",
        "affected" => $mysqli->affected_rows
    ];
}

function resumirResultadosIA(
    string $ollamaUrl,
    string $model,
    string $peticionUsuario,
    string $sql,
    array $rows,
    int $maxRows = 20,
    int $maxChars = 8000
): string {

    if(empty($rows)){
        return "No se han encontrado resultados para la consulta.";
    }

    $sample = array_slice($rows, 0, $maxRows);
    $json = json_encode($sample, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
    if($json === false) $json = "[]";
    if(strlen($json) > $maxChars){
        $json = substr($json, 0, $maxChars) . "\n... (recortado)";
    }

    $total = count($rows);
    $cols  = array_keys($rows[0] ?? []);
    $colsS = implode(", ", $cols);

    $prompt = "
Eres un asistente que redacta un breve comentario-resumen, en español, sobre unos resultados de base de datos.

Contexto:
- Petición del usuario: {$peticionUsuario}
- SQL ejecutado: {$sql}
- Total de filas: {$total}
- Columnas: {$colsS}

Muestra de filas (JSON):
{$json}

Instrucciones:
- Devuelve SOLO el comentario.
- Máximo 3-5 frases.
- No inventes datos que no estén en la muestra.
- Si detectas patrones obvios (valores repetidos, rangos de fechas), menciónalos con cautela.
";

    $r = llamarOllama($ollamaUrl, $model, $prompt, 120);
    if(!$r["ok"]){
        return "Resumen no disponible (error al consultar el modelo).";
    }

    $txt = trim((string)$r["response"]);
    return $txt !== "" ? $txt : "Resumen no disponible (respuesta vacía del modelo).";
}

/* ================================
   GRÁFICAS (SVG tarta interactiva)
================================ */

function detectarColumnasRepetibles(array $rows, int $maxDistinct = 12, int $minRepeat = 2): array {
    if (empty($rows)) return [];

    $cols = array_keys($rows[0]);
    $candidatas = [];

    foreach ($cols as $col) {
        $counts = [];

        foreach ($rows as $r) {
            $v = $r[$col] ?? null;

            if ($v === null) {
                $v = "(NULL)";
            } else {
                $v = trim((string)$v);
                if ($v === "") $v = "(vacío)";
            }

            $counts[$v] = ($counts[$v] ?? 0) + 1;
        }

        $distinct = count($counts);
        if ($distinct <= 1) continue;

        $allNumeric = true;
        foreach (array_keys($counts) as $k) {
            if ($k === "(NULL)" || $k === "(vacío)") {
                $allNumeric = false;
                break;
            }

            $ks = (string)$k;
            $k2 = str_replace([',', ' '], ['.', ''], $ks);

            if (!is_numeric($k2)) {
                $allNumeric = false;
                break;
            }
        }
        if ($allNumeric && $distinct > 6) continue;
        if ($distinct > $maxDistinct)     continue;

        $hasRepeat = false;
        foreach ($counts as $c) {
            if ($c >= $minRepeat) { $hasRepeat = true; break; }
        }
        if (!$hasRepeat) continue;

        arsort($counts);

        $candidatas[] = [
            "col"    => $col,
            "counts" => $counts
        ];
    }

    usort($candidatas, function($a, $b){
        $aTop = (int)reset($a["counts"]);
        $bTop = (int)reset($b["counts"]);
        $aDistinct = count($a["counts"]);
        $bDistinct = count($b["counts"]);

        if ($aTop !== $bTop) return $bTop <=> $aTop;
        return $aDistinct <=> $bDistinct;
    });

    return $candidatas;
}

function clamp01(float $x): float { return max(0.0, min(1.0, $x)); }

function colorPorIndice(int $i, int $n): string {
    $n = max(1, $n);
    $h = ($i * (360.0 / $n));
    $s = 0.62;
    $l = 0.52;

    $c = (1 - abs(2*$l - 1)) * $s;
    $x = $c * (1 - abs(fmod($h/60.0, 2) - 1));
    $m = $l - $c/2;

    $r=$g=$b=0.0;
    if($h < 60){ $r=$c; $g=$x; $b=0; }
    elseif($h < 120){ $r=$x; $g=$c; $b=0; }
    elseif($h < 180){ $r=0; $g=$c; $b=$x; }
    elseif($h < 240){ $r=0; $g=$x; $b=$c; }
    elseif($h < 300){ $r=$x; $g=0; $b=$c; }
    else { $r=$c; $g=0; $b=$x; }

    $R = (int)round(255*clamp01($r+$m));
    $G = (int)round(255*clamp01($g+$m));
    $B = (int)round(255*clamp01($b+$m));

    return sprintf("#%02X%02X%02X", $R, $G, $B);
}

function svgPieSlicePath(float $cx, float $cy, float $r, float $a0, float $a1): string {
    $x0 = $cx + $r * cos($a0);
    $y0 = $cy + $r * sin($a0);
    $x1 = $cx + $r * cos($a1);
    $y1 = $cy + $r * sin($a1);
    $largeArc = (($a1 - $a0) > M_PI) ? 1 : 0;

    return sprintf(
        "M %.3f %.3f L %.3f %.3f A %.3f %.3f 0 %d 1 %.3f %.3f Z",
        $cx, $cy, $x0, $y0, $r, $r, $largeArc, $x1, $y1
    );
}

function renderPieChartSVG(string $id, string $titulo, array $counts): string {
    $total = array_sum($counts);
    if($total <= 0) return "";

    $w = 520; $h = 280;
    $cx = 140; $cy = 140; $r = 110;

    $labels = array_keys($counts);
    $n = count($labels);

    $out  = '';
    $out .= '<div class="chart-card" id="'.h($id).'-card">';
    $out .=   '<div class="chart-title">'.h($titulo).'</div>';
    $out .=   '<div class="chart-wrap">';
    $out .=     '<svg class="chart-svg" width="'.$w.'" height="'.$h.'" viewBox="0 0 '.$w.' '.$h.'" role="img" aria-label="'.h($titulo).'">';
    $out .=       '<defs>';
    $out .=         '<filter id="'.h($id).'-shadow" x="-30%" y="-30%" width="160%" height="160%">';
    $out .=           '<feDropShadow dx="0" dy="2" stdDeviation="2" flood-opacity="0.18"/>';
    $out .=         '</filter>';
    $out .=       '</defs>';

    $out .=       '<g filter="url(#'.h($id).'-shadow)">';
    $a = -M_PI/2;
    $idx = 0;

    foreach($counts as $label => $c){
        $frac = $c / $total;
        $a1 = $a + $frac * 2 * M_PI;

        $path  = svgPieSlicePath($cx, $cy, $r, $a, $a1);
        $color = colorPorIndice($idx, $n);
        $pct   = round($frac*100, 1);

        $out .= '<path class="slice" data-chart="'.h($id).'" data-key="'.h($label).'" data-count="'.h((string)$c).'" data-pct="'.h((string)$pct).'" d="'.$path.'" fill="'.$color.'" stroke="#ffffff" stroke-width="1.2"></path>';

        $a = $a1;
        $idx++;
    }
    $out .=       '</g>';

    $out .=       '<g class="tooltip" id="'.h($id).'-tt" style="display:none;">';
    $out .=         '<rect class="tt-bg" x="0" y="0" rx="6" ry="6" width="10" height="10"></rect>';
    $out .=         '<text class="tt-text" x="0" y="0">-</text>';
    $out .=       '</g>';

    $out .=     '</svg>';

    $out .=     '<div class="chart-legend" id="'.h($id).'-legend">';
    $idx = 0;
    foreach($counts as $label => $c){
        $color = colorPorIndice($idx, $n);
        $out .= '<button type="button" class="legend-item" data-chart="'.h($id).'" data-key="'.h($label).'" aria-pressed="true">';
        $out .=   '<span class="swatch" style="background:'.$color.'"></span>';
        $out .=   '<span class="lab">'.h($label).'</span>';
        $out .=   '<span class="val">'.h((string)$c).'</span>';
        $out .= '</button>';
        $idx++;
    }
    $out .=     '</div>';

    $out .=   '</div>';
    $out .= '</div>';

    return $out;
}

/* ================================
   PROCESAMIENTO
================================ */

$sql_generado = "";
$resultado_db = null;
$error = "";
$resumen_ia = "";
$charts_html = "";
$exec_time = null;
$row_count = null;

if($_SERVER["REQUEST_METHOD"] === "POST" && !empty($_POST["peticion"])){

    $peticion = trim($_POST["peticion"]);

    $prompt = "
Tengo una base de datos que tiene una tabla clientes con esta estructura:

CREATE TABLE clientes (
  id INT(11) NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255),
  apellidos VARCHAR(255),
  email VARCHAR(255),
  poblacion VARCHAR(255),
  fecha_de_nacimiento DATE,
  PRIMARY KEY (id)
);

Lo que quiero es que me des el SQL para responder a
la siguiente petición por parte del usuario:

".$peticion."

Lo que necesito es que me des el codigo SQL para esa peticion.
No me des nada más que código SQL. Tampoco quiero fences.
Cuando hagas consultas con Where, usa WHERE x LIKE '%y%'.
El codigo resultante debe ser SQL puro, nunca markdown.
";

    $r = llamarOllama($OLLAMA_URL, $MODEL, $prompt, 120);
    if(!$r["ok"]){
        $error = $r["error"];
    } else {
        $sql_generado = trim($r["response"] ?? "");

        // 1) Nos quedamos solo con la primera sentencia por seguridad
        $parts = preg_split('/;[\r\n]*/', $sql_generado);
        $sql_generado = trim($parts[0] ?? "");

        if($sql_generado === ""){
            $error = "El modelo no devolvió una sentencia SQL no vacía.";
        } elseif(!preg_match("/^(SELECT|INSERT|UPDATE|DELETE)/i", $sql_generado)){
            $error = "El modelo no devolvió una sentencia SQL válida.";
        } else {

            // 2) Si es SELECT y no lleva LIMIT, añadimos LIMIT defensivo
            if (preg_match('/^SELECT/i', $sql_generado) && !preg_match('/\bLIMIT\b/i', $sql_generado)) {
                $sql_generado .= " LIMIT 200";
            }

            // 3) Ejecutar midiendo tiempo
            $t0 = microtime(true);
            $resultado_db = ejecutarSQL(
                $sql_generado,
                $db_host,
                $db_user,
                $db_pass,
                $db_name
            );
            $exec_time = microtime(true) - $t0;

            if(is_array($resultado_db) && ($resultado_db["type"] ?? "") === "select"){
                $rows = $resultado_db["data"] ?? [];
                $row_count = count($rows);

                // Resumen IA
                $resumen_ia = resumirResultadosIA(
                    $OLLAMA_URL,
                    $MODEL,
                    $peticion,
                    $sql_generado,
                    $rows
                );

                // Gráficas
                $candidatas = detectarColumnasRepetibles($rows, 12, 2);
                $candidatas = array_slice($candidatas, 0, 4);

                if(!empty($candidatas)){
                    $charts_html .= '<div class="charts-grid">';
                    $i = 1;
                    foreach($candidatas as $c){
                        $col     = (string)$c["col"];
                        $counts  = (array)$c["counts"];
                        $chartId = "chart_".$i;
                        $charts_html .= renderPieChartSVG($chartId, "Distribución por: ".$col, $counts);
                        $i++;
                    }
                    $charts_html .= '</div>';
                }
            }
        }
    }
}
?>
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>SaasIA SQL Runner</title>
<style>
body{
    margin:0;
    font-family:Arial, Helvetica, sans-serif;
    background:#f5f6f8;
    color:#222;
}

header{
    background:#1f2937;
    color:white;
    padding:20px;
}

main{
    padding:30px;
    max-width:1100px;
    margin:auto;
}

/* Tarjetas */
.card{
    background:#ffffff;
    padding:18px;
    border-radius:8px;
    box-shadow:0 2px 6px rgba(0,0,0,0.08);
    border:1px solid #e5e7eb;
    margin-bottom:18px;
}

.card h2{
    margin-top:0;
    margin-bottom:10px;
    font-size:18px;
    color:#1f2937;
    border-bottom:2px solid #e5e7eb;
    padding-bottom:6px;
}

/* Formulario */
form{
    display:flex;
    gap:10px;
    margin-bottom:0;
}

input[type=text]{
    flex:1;
    padding:12px;
    border:1px solid #ccc;
    border-radius:4px;
    font-size:16px;
}

button{
    padding:12px 20px;
    border:none;
    background:#2563eb;
    color:white;
    border-radius:4px;
    cursor:pointer;
    font-size:15px;
}

button:hover{
    background:#1d4ed8;
}

/* SQL generado */
.sql-box{
    background:#111827;
    color:#10b981;
    padding:15px;
    font-family:monospace;
    border-radius:4px;
    margin-top:8px;
    white-space:pre-wrap;
}

/* Botón copiar */
.copy-btn{
    float:right;
    margin-top:-34px;
    background:#3b82f6;
    padding:6px 10px;
    font-size:13px;
    border-radius:4px;
}

.copy-btn:hover{
    background:#1d4ed8;
}

/* Mensajes */
.info{
    background:#ecfdf5;
    padding:10px;
    border:1px solid #10b981;
    border-radius:4px;
    margin-bottom:14px;
}

.error{
    background:#fee2e2;
    padding:10px;
    border:1px solid #dc2626;
    border-radius:4px;
    margin-bottom:14px;
}

.summary{
    background:#eff6ff;
    padding:12px;
    border:1px solid #2563eb;
    border-radius:4px;
    margin: 0 0 8px 0;
    line-height:1.45;
}

/* Tabla */
table{
    width:100%;
    border-collapse:collapse;
    background:white;
    box-shadow:0 2px 6px rgba(0,0,0,0.08);
}

th{
    background:#e5e7eb;
    text-align:left;
    padding:10px;
    font-weight:bold;
    font-size:14px;
}

td{
    padding:10px;
    border-top:1px solid #eee;
    font-size:14px;
}

tr:hover{
    background:#f9fafb;
}

/* ======= CHARTS ======= */
.charts-grid{
    display:grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap:14px;
    margin: 0 0 14px 0;
}

@media (max-width: 980px){
    .charts-grid{ grid-template-columns: 1fr; }
}

.chart-card{
    background:#fff;
    border:1px solid #e5e7eb;
    border-radius:8px;
    box-shadow:0 2px 6px rgba(0,0,0,0.06);
    padding:12px;
}

.chart-title{
    font-weight:700;
    font-size:14px;
    margin: 0 0 10px 0;
    color:#111827;
}

.chart-wrap{
    display:flex;
    gap:12px;
    align-items:flex-start;
}

.chart-svg{
    flex: 0 0 auto;
    border-radius:8px;
    background:#fafafa;
    border:1px solid #f0f0f0;
}

.slice{
    cursor:pointer;
    transition: transform 120ms ease, opacity 120ms ease;
    transform-origin: 140px 140px;
}

.slice:hover{
    transform: scale(1.02);
}

.slice.is-off{
    opacity: 0.10;
}

.chart-legend{
    display:flex;
    flex-direction:column;
    gap:8px;
    min-width: 240px;
    max-height: 280px;
    overflow:auto;
    padding-right:4px;
}

.legend-item{
    display:grid;
    grid-template-columns: 14px 1fr auto;
    gap:8px;
    align-items:center;
    padding:8px;
    border:1px solid #e5e7eb;
    background:#fff;
    border-radius:8px;
    cursor:pointer;
    text-align:left;
}

.legend-item:hover{
    background:#f9fafb;
}

.legend-item[aria-pressed="false"]{
    opacity:0.55;
}

.swatch{
    width:12px;
    height:12px;
    border-radius:3px;
    border:1px solid rgba(0,0,0,0.08);
}

.lab{
    font-size:13px;
    color:#111827;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}

.val{
    font-size:12px;
    color:#374151;
}

/* Tooltip in SVG */
.tooltip .tt-bg{
    fill:#111827;
    opacity:0.92;
}
.tooltip .tt-text{
    fill:#ffffff;
    font-size:12px;
    font-family:Arial, Helvetica, sans-serif;
}
</style>
</head>
<body>

<header>
    <h1>SaasIA - Generador y Ejecutor SQL</h1>
</header>

<main>

    <!-- CARD: Generar consulta -->
    <div class="card">
        <h2>Generar consulta SQL</h2>
        <form method="POST">
            <input type="text" name="peticion" placeholder="Ej: clientes de Valencia" value="<?= h($_POST["peticion"] ?? "") ?>">
            <button type="submit">Ejecutar</button>
        </form>
    </div>

    <!-- CARD: SQL generado -->
    <?php if($sql_generado): ?>
        <div class="card">
            <h2>SQL generado</h2>
            <button type="button" class="copy-btn" onclick="copySQL()">Copiar SQL</button>
            <pre id="sql-box" class="sql-box"><?= h($sql_generado) ?></pre>
        </div>
    <?php endif; ?>

    <!-- ERRORES -->
    <?php if($error): ?>
        <div class="error"><?= h($error) ?></div>
    <?php endif; ?>

    <!-- RESULTADOS -->
    <?php if($resultado_db): ?>

        <?php if(isset($resultado_db["error"])): ?>
            <div class="error"><?= h($resultado_db["error"]) ?></div>

        <?php elseif(($resultado_db["type"] ?? "") === "select"): ?>

            <?php if(!empty($resumen_ia)): ?>
                <div class="card">
                    <h2>Resumen de resultados</h2>
                    <div class="summary"><?= h($resumen_ia) ?></div>
                </div>
            <?php endif; ?>

            <?php if(!empty($charts_html)): ?>
                <div class="card">
                    <h2>Gráficas interactivas</h2>
                    <?= $charts_html ?>
                </div>
            <?php endif; ?>

            <?php if(empty($resultado_db["data"])): ?>
                <div class="info">Consulta ejecutada correctamente. Sin resultados.</div>
            <?php else: ?>

                <?php
                    $allRows   = $resultado_db["data"];
                    $shownRows = array_slice($allRows, 0, 500);
                    $totalRows = $row_count ?? count($allRows);
                ?>
                <div class="card">
                    <h2>Tabla de resultados</h2>

                    <div class="info">
                        Filas devueltas: <?= h((string)$totalRows) ?>
                        <?php if($exec_time !== null): ?>
                            · Tiempo de ejecución: <?= h(number_format($exec_time * 1000, 2)) ?> ms
                        <?php endif; ?>
                    </div>

                    <table>
                        <thead>
                            <tr>
                                <?php foreach(array_keys($shownRows[0]) as $col): ?>
                                    <th><?= h($col) ?></th>
                                <?php endforeach; ?>
                            </tr>
                        </thead>
                        <tbody>
                            <?php foreach($shownRows as $fila): ?>
                                <tr>
                                    <?php foreach($fila as $valor): ?>
                                        <td><?= h($valor) ?></td>
                                    <?php endforeach; ?>
                                </tr>
                            <?php endforeach; ?>
                        </tbody>
                    </table>

                    <?php if(count($allRows) > count($shownRows)): ?>
                        <div class="info" style="margin-top:10px;">
                            Mostrando solo las primeras <?= h((string)count($shownRows)) ?> filas
                            de un total de <?= h((string)count($allRows)) ?>.
                        </div>
                    <?php endif; ?>
                </div>

            <?php endif; ?>

        <?php elseif(($resultado_db["type"] ?? "") === "action"): ?>
            <div class="card">
                <h2>Resultado de la operación</h2>
                <div class="info">
                    Sentencia ejecutada correctamente.
                    Filas afectadas: <?= h($resultado_db["affected"] ?? 0) ?>
                </div>
            </div>
        <?php endif; ?>

    <?php endif; ?>

</main>

<script>
(function(){
  function qs(sel, root){ return (root || document).querySelector(sel); }
  function qsa(sel, root){ return Array.from((root || document).querySelectorAll(sel)); }

  function setTooltip(svg, tt, x, y, text){
    const txt = tt.querySelector(".tt-text");
    const bg  = tt.querySelector(".tt-bg");

    txt.textContent = text;

    tt.style.display = "block";
    txt.setAttribute("x", 0);
    txt.setAttribute("y", 0);

    const bbox = txt.getBBox();
    const padX = 10, padY = 8;

    bg.setAttribute("x", bbox.x - padX);
    bg.setAttribute("y", bbox.y - padY);
    bg.setAttribute("width", bbox.width + padX*2);
    bg.setAttribute("height", bbox.height + padY*2);

    const vb = svg.viewBox.baseVal;
    const w = vb && vb.width ? vb.width : svg.clientWidth;
    const h = vb && vb.height ? vb.height : svg.clientHeight;

    let tx = x + 12;
    let ty = y - 12;

    const tw = bbox.width + padX*2;
    const th = bbox.height + padY*2;

    if(tx + tw > w) tx = x - tw - 12;
    if(ty - th < 0) ty = y + th;

    tt.setAttribute("transform", `translate(${tx},${ty})`);
  }

  function hideTooltip(tt){
    if(tt) tt.style.display = "none";
  }

  // Hover tooltip on slices
  qsa("svg.chart-svg").forEach(svg => {
    const tt = svg.querySelector("g.tooltip");
    qsa("path.slice", svg).forEach(p => {
      p.addEventListener("mousemove", (ev) => {
        const pt = svg.createSVGPoint();
        pt.x = ev.clientX; pt.y = ev.clientY;
        const ctm = svg.getScreenCTM();
        if(!ctm) return;
        const loc = pt.matrixTransform(ctm.inverse());

        const key = p.getAttribute("data-key") || "";
        const cnt = p.getAttribute("data-count") || "0";
        const pct = p.getAttribute("data-pct") || "0";
        setTooltip(svg, tt, loc.x, loc.y, `${key}: ${cnt} (${pct}%)`);
      });

      p.addEventListener("mouseleave", () => hideTooltip(tt));
    });

    svg.addEventListener("mouseleave", () => hideTooltip(tt));
  });

  // Legend toggle => hide/show slice
  qsa(".legend-item").forEach(btn => {
    btn.addEventListener("click", () => {
      const chart = btn.getAttribute("data-chart");
      const key   = btn.getAttribute("data-key");
      if(!chart || !key) return;

      const pressed = btn.getAttribute("aria-pressed") !== "false";
      const next = !pressed;
      btn.setAttribute("aria-pressed", next ? "true" : "false");

      const slice = document.querySelector(`path.slice[data-chart="${CSS.escape(chart)}"][data-key="${CSS.escape(key)}"]`);
      if(slice){
        slice.classList.toggle("is-off", !next);
      }
    });
  });
})();

// Copiar SQL al portapapeles
function copySQL(){
  const box = document.getElementById('sql-box');
  if(!box) return;
  const text = box.innerText || box.textContent || '';
  if(navigator.clipboard){
    navigator.clipboard.writeText(text);
  } else {
    // Fallback simple
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch(e){}
    document.body.removeChild(ta);
  }
}
</script>

</body>
</html>
