<!DOCTYPE html>
<html>
<head>
    <title>Kalkulator HPP Full Costing</title>
    <style>
        body {
            font-family: Arial;
            max-width: 600px;
            margin: auto;
            padding: 20px;
        }
        input {
            width: 100%;
            padding: 8px;
            margin: 5px 0;
        }
        button {
            padding: 10px;
            width: 100%;
            margin-top: 10px;
            background: #4CAF50;
            color: white;
            border: none;
        }
        .box {
            padding: 15px;
            background: #f4f4f4;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<h2>Kalkulator HPP Metode Full Costing</h2>

<label>Biaya Bahan Baku (Rp)</label>
<input type="number" id="bahan">

<label>Biaya Tenaga Kerja Langsung (Rp)</label>
<input type="number" id="tkl">

<label>Biaya Overhead Pabrik (Rp)</label>
<input type="number" id="bop">

<label>Jumlah Produksi (Unit)</label>
<input type="number" id="unit">

<button onclick="hitungHPP()">Hitung HPP</button>

<div class="box" id="hasil"></div>

<script>
function hitungHPP() {
    let bahan = parseFloat(document.getElementById("bahan").value);
    let tkl = parseFloat(document.getElementById("tkl").value);
    let bop = parseFloat(document.getElementById("bop").value);
    let unit = parseFloat(document.getElementById("unit").value);

    let totalBiayaProduksi = bahan + tkl + bop;
    let hppPerUnit = totalBiayaProduksi / unit;
    let hargaJual = hppPerUnit * 1.30; // markup 30%

    document.getElementById("hasil").innerHTML = `
        <b>Total Biaya Produksi:</b> Rp ${totalBiayaProduksi.toLocaleString()} <br>
        <b>HPP per Unit:</b> Rp ${hppPerUnit.toLocaleString()} <br>
        <b>Harga Jual (Markup 30%):</b> Rp ${hargaJual.toLocaleString()}
    `;
}
</script>

</body>
</html>
