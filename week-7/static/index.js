function submit(){
    const username=document.getElementById("username").value;
    fetch('http://127.0.0.1:3000/api/members?username='+username)
  .then(function(response) {
    return response.json();
  })
  .then(function(result) {
    document.getElementById("username_result").innerHTML=result.data.name+"("+result.data.username+")";
  })
  .catch(function(error) {
    document.getElementById("username_result").innerHTML="無此人註冊"
  });
  
}

function update(){
    const update_name=document.getElementById("update_name").value;
    let url='http://127.0.0.1:3000/api/member';
    fetch(url, {
        method:'POST',
        body:JSON.stringify({"name":update_name
        }),
        headers: {
          'Content-Type':'application/json'
        }
      })
      .then(res => {
          return res.json();   
      }).then(result => {
            console.log(result)
            if(result["OK"]==true){
                document.getElementById("update_result").innerHTML="更新成功";
            }    
      })
      .catch(result => {
            if(result["error"]==true){
                document.getElementById("update_result").innerHTML="更新失敗";
        }   
      });
}

