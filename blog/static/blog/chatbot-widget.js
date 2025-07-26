(function() {
    // チャットボタン
    const button = document.createElement("div");
    button.innerText = "💬 ご質問はこちら";
    button.style.position = "fixed";
    button.style.bottom = "20px";
    button.style.right = "20px";
    button.style.background = "#007bff";
    button.style.color = "white";
    button.style.padding = "10px 15px";
    button.style.borderRadius = "20px";
    button.style.cursor = "pointer";
    button.style.boxShadow = "0 0 10px rgba(0,0,0,0.2)";
    document.body.appendChild(button);
  
    // チャットウィンドウ iframe
    const iframe = document.createElement("iframe");
    iframe.src = "https://あなたのドメイン/blog/chatbot/";
    iframe.style.position = "fixed";
    iframe.style.bottom = "70px";
    iframe.style.right = "20px";
    iframe.style.width = "350px";
    iframe.style.height = "500px";
    iframe.style.border = "1px solid #ccc";
    iframe.style.borderRadius = "10px";
    iframe.style.boxShadow = "0 0 15px rgba(0,0,0,0.3)";
    iframe.style.display = "none";
    iframe.style.zIndex = "10000";
    document.body.appendChild(iframe);
  
    button.addEventListener("click", function() {
      iframe.style.display = iframe.style.display === "none" ? "block" : "none";
    });
  })();
  

  <script src="https://あなたのドメイン/static/blog/chatbot-widget.js"></script>
