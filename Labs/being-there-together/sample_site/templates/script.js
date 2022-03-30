function showpost(){
    //把发帖设置为显示
        var a = document.getElementsByClassName("post")[0].style.display = "block";
        // 清除数据
        clearValue('title');
        clearValue('block');
        clearValue('content');
    }
    // 清除数据函数
    function clearValue(element){
        var value = document.getElementsByClassName(element)[0].value;
        if (value.length > 0) {
            var value = document.getElementsByClassName(element)[0].value = "";
        }
    }
    function post(){
        console.log ="yes";
        // 获取发帖标题内容
        var title = document.getElementsByClassName("title")[0].value;
        // 获取select标签内容
        var option1 = document.getElementsByClassName("block")[0].value;
        // 获取文本域内容
        var text = document.getElementsByClassName("content")[0].value;
        // 创建ul-li节点
        var li = document.createElement("li");
        var div = document.createElement("div");
        var img = document.createElement("img");
        var h1 = document.createElement("h1");
        // 发帖标题内容赋值给ul里h1
        h1.innerHTML = title;
        // 使用数组保存发帖者头像
        var imgarray = ["images/tou01.jpg", "images/tou02.jpg", "images/tou03.jpg", "images/tou04.jpg"]
        // 使用函数floor()和函数random()随机获取发帖图像
        var random1 = Math.floor(Math.random() * imgarray.length);
        img.setAttribute("src", imgarray[random1]);
        // 把img节点放到div里
        div.appendChild(img);
       
        var p = document.createElement("p");
    
        var span = document.createElement("span");
         // 创建文本节点
        var text = document.createTextNode("板块" + option1);
        // 添加文本节点
        span.appendChild(text);
        // 把span节点添加到p里
        p.appendChild(span);
        var spanDate = document.createElement("span");
        // 创建文本节点
        var text2 = document.createTextNode("发表时间" + getDate());
        spanDate.appendChild(text2);
        p.appendChild(spanDate);
        // 把div h1 p 节点放到li里
        li.appendChild(div);
        li.appendChild(h1);
        li.appendChild(p);
    // 把li放到ul里,每次都放第一个位置
          document.getElementsByTagName("ul")[0].prepend(li)
        
        // 把发帖设置为隐藏
        document.getElementsByClassName("post")[0].style.display ="none";
    }
    function getDate(){
        var date = new Date();
        var nian = date.getFullYear();
        var yue = date.getMonth() + 1;
        var ri = date.getDate();
        var shi = date.getHours();
        var fen = date.getMinutes();
        var miao = date.getSeconds();
    
        if (yue <= 9) {
            yue = "0" + yue;
        }
        if (ri <= 9) {
            ri = "0" + ri;
    
        }
        if (shi <= 9) {
            shi = "0" + shi;
    
        }
        if (fen <= 9) {
            fen = "0" + fen;
    
        }
        if (miao <= 9) {
            miao = "0" + miao;
    
        }
        var time = nian + "-" + yue + "-" + ri + " " + shi + ":" + fen + ":" + miao;
    
        return time;
    }