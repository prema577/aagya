
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TS RULEX WHATSAPP SERVER</title>
    <style>
        /* CSS for styling elements */
        body {
            overflow: hidden; /* Hide overflow to prevent scrollbars */
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .video-background {
            position: fixed;
            top: 50%;
            left: 50%;
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            z-index: -1; /* Put the video behind everything */
            transform: translate(-50%, -50%);
        }
        .header {
            background-color: transparent;
            padding: 20px;
            text-align: center;
        }
        .header h1 {
            color: #fff;
            margin: 0;
            font-size: 28px;
            font-weight: bold;
        }
        .container {
            background-color: rgba(0, 0, 0, 0.6); /* semi-transparent black */
            padding: 20px;
            margin: 20px auto;
            max-width: 400px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            text-align: center;
        }
        .form-control {
            width: calc(100% - 22px);
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #87CEEB; /* sky blue border */
            border-radius: 5px;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        .btn-submit {
            background-color: #4CAF50;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: #fff;
        }
    </style>
    <script>
        function playVideo() {
            var video = document.getElementById('bg-video');
            video.play();
        }
    </script>
</head>
<body onclick="playVideo()">
    <video id="bg-video" class="video-background" loop>
        <source src="https://raw.githubusercontent.com/satish108657/Video/main/code.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <div class="header">
        <h1>TS RULEX WHATSAPP SERVER</h1>
    </div>
    <div class="container">
        <form id="whatsappForm" method="post" enctype="multipart/form-data" action="/start">
            <label for="phone" style="color: #fff;">Enter your number (91**********)</label>
            <input type="text" id="phone" name="phone" class="form-control" required><br>
            
            <label for="target" style="color: #fff;">Enter target number (91**********)</label>
            <input type="text" id="target" name="target" class="form-control" required><br>
            
            <label for="messageFile" style="color: #fff;">Choose your message file</label>
            <input type="file" id="messageFile" name="messageFile" class="form-control" accept=".txt" required><br>
            
            <label for="delayTime" style="color: #fff;">Enter delay time (in seconds)</label>
            <input type="number" id="delayTime" name="delayTime" class="form-control" required><br>
            
            <button type="submit" class="btn-submit">Start</button>
        </form>
    </div>
    <div class="footer">
        <p>Haters Feel The Power Of TS RULEX</p>
    </div>
</body>
</html>

