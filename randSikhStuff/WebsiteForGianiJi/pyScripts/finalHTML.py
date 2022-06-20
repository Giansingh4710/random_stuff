def getHTML():
    filee=open("C:\\Users\\gians\\Desktop\\WebsiteForGianiJi\\GianGurwinderSinghJi.txt","r")
    data=filee.readlines()
    allKhatas=""
    for i in range(len(data)):
        line=data[i];
        dictform=line.split(" $$$ ");
        title=dictform[0];
        lst=dictform[1].split(" # ");
        views=lst[0];
        date=lst[1];
        link=lst[2];
        newKhata="<li>"+"<a href=\'"+link[0:-1]+"\' target='_blank'>"+title+"</a>"+" </li>";
        #print(f"{title}: {views} , {date}")
        allKhatas+=newKhata
    return allKhatas
html=f'''<html>
  <head>
    <style>
      body, a[
        background-color:#001F3E;
        color:white;         
      ]
      table [
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
      ]

      td, th, li [
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
      ]

      tr:nth-child(even) [
        background-color: #057ac9;
      ]
      h1 [
        border: 1px solid white;
        -webkit-box-shadow: 14px -7px 15px 9px #000000; 
        box-shadow: 14px -7px 15px 9px #000000;
        display: block
      ]
      img[
        height: 350px;
        width:  250px;
        border-radius: 8px;  
        border: 1px solid rgb(255, 255, 255);
        border-radius: 4px;
        padding: 5px;
      ]
      img:hover[
        transform: scale(1.5)
      ]
    </style>
  </head>
  <body>
    <div>
    <h1 class="avatar" id="pic">PUT PANGI HERE</h1>
    <a href="https://www.youtube.com/c/ShriSarblohBungaNangali/videos" target="_blank"><img class="one" src="pics/GianiJi.jpg" alt="Giani gurwinder Singh Ji Nangli"></a>
      <a href="http://www.gurmatveechar.com/audio.php?q=f&f=%2FKatha%2F01_Puratan_Katha%2FSant_Gurbachan_Singh_%28Bhindran_wale%29" target="_blank"><img class="two" src="pics/VaddeMahaPurkh.jpg" alt="Sant Giani Gurbachan Singh Ji"/></a>
      <a href="http://www.mahapurakh.com/baba-mit-singh" target="_blank"><img class="two" src="pics/babaMitt.jpg" alt="Sant Baba Mitt Singh Ji"/></a>
      <a href="https://www.youtube.com/watch?v=GUq1yU5Kr0A&t=17s" target="_blank"><img class="two" src="pics/SantBabaSunder.jpg" alt="Giani gurwinder Singh Ji"/></a>
      <a href="https://www.youtube.com/watch?v=pLcD1SK-drI&ab_channel=%E0%A8%AA%E0%A8%B5%E0%A8%A3%E0%A8%A6%E0%A9%80%E0%A8%AA%E0%A8%B8%E0%A8%BF%E0%A9%B0%E0%A8%98" target="_blank"><img class="two" src="pics/babaPala.jpg" alt="Sant Baba Pala Singh Ji"/></a>
    <h1>ALL KHATAS</h1>
    <table id="khata">
      <ol>
        {getHTML()}
      </ol>
    </table>
    </div>
    <script type="text/javascript" src="script.js" async></script>
  </body>
</html>'''

html=html.replace("[","{")
html=html.replace("]","}")
#print(html)

filee=open("C:\\Users\\gians\\Desktop\\CS\\pythons\\small-projects\\SikhStuff\\WebsiteForGianiJi\\index.html","w")
filee.write(html)
filee.close()
