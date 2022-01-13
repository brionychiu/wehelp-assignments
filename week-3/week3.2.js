let req=new XMLHttpRequest();
req.open("get","https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json");
req.send();
req.onload=function(){
    let data = JSON.parse(req.responseText);
    let info=data.result.results;
    let n=0;
    for(let i=n;i<n+8;i++){
        let newDiv = document.createElement('div');
        newDiv.setAttribute("class","item2");
        let newImg = document.createElement('img');
        let pic=info[i].file.replace(/JPG/g,"jpg");
        pic=pic.split("jpg");
        pic=pic[0]+"jpg";
        newImg.setAttribute('src',pic);
        newImg.setAttribute("class","photo");
        newDiv.appendChild(newImg);
        let textNode=document.createTextNode(info[i].stitle);
        newDiv.appendChild(textNode);
        document.getElementById("myList0").appendChild(newDiv);
    };
};
function init(){
    let btn=document.getElementById("btn");
    let n=8;
    let handler=function(){
        let req=new XMLHttpRequest();
        req.open("get","https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json");
        req.send();
        req.onload=function(){
            let data = JSON.parse(req.responseText);
            let info=data.result.results;
            for(let i=n;i<n+8;i++){
                let newDiv = document.createElement('div');
                newDiv.setAttribute("class","item2");
                let newImg = document.createElement('img');
                let pic=info[i].file.replace(/JPG/g,"jpg");
                pic=pic.split("jpg");
                pic=pic[0]+"jpg";
                newImg.setAttribute('src',pic);
                newImg.setAttribute("class","photo");
                newDiv.appendChild(newImg);
                let textNode=document.createTextNode(info[i].stitle);
                newDiv.appendChild(textNode);
                document.getElementById("myList0").appendChild(newDiv);
            };
            n=n+8;

        };        
    };
    btn.addEventListener("click",handler);
};