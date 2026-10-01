<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Are you free?</title>
  <style>
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      font-family: 'Arial', sans-serif;
      background-color: #ffe6e8;
      text-align: center;
    }

    .container {
      background: white;
      padding: 40px;
      border-radius: 20px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.1);
      max-width: 90%;
    }

    h1 {
      color: #ff4b6e;
      font-size: 2.5rem;
      margin-bottom: 30px;
    }

    .buttons {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
    }

    button {
      padding: 12px 25px;
      font-size: 1.2rem;
      border: none;
      border-radius: 10px;
      cursor: pointer;
      transition: transform 0.2s ease, font-size 0.2s ease;
    }

    #yesBtn {
      background-color: #4caf50;
      color: white;
      font-weight: bold;
    }

    #noBtn {
      background-color: #f44336;
      color: white;
      font-weight: bold;
    }

    /* Message Page (Nakatago sa simula) */
    #nextPage {
      display: none;
    }

    #nextPage h1 {
      color: #ff4b6e;
    }
  </style>
</head>
<body>

  <!-- First Page -->
  <div class="container" id="mainPage">
    <h1>Are you free on Oct 21? 🌹</h1>
    <div class="buttons">
      <button id="yesBtn" onclick="goToNextPage()">YES</button>
      <button id="noBtn" onclick="growYes()">NO</button>
    </div>
  </div>

  <!-- Next Page (lalabas kapag na-click ang YES) -->
  <div class="container" id="nextPage">
    <h1>Yaaay! See you on Oct 21! 🎉✨</h1>
    <p style="font-size: 1.3rem; color: #555;">It's a date! ❤️</p>
  </div>

  <script>
    let yesPaddingVertical = 12;
    let yesPaddingHorizontal = 25;
    let yesFontSize = 1.2;

    function growYes() {
      // Pinapalaki ang YES button sa bawat click ng NO
      yesPaddingVertical += 10;
      yesPaddingHorizontal += 20;
      yesFontSize += 0.4;

      const yesBtn = document.getElementById("yesBtn");
      yesBtn.style.padding = `${yesPaddingVertical}px ${yesPaddingHorizontal}px`;
      yesBtn.style.fontSize = `${yesFontSize}rem`;
    }

    function goToNextPage() {
      // Itatago ang unang page at ipapakita ang next page
      document.getElementById("mainPage").style.display = "none";
      document.getElementById("nextPage").style.display = "block";
    }
  </script>

</body>
</html>
