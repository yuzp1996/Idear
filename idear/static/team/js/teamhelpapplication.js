/**
 * Created by admin on 2017/7/23.
 */
$("body").on("click","#allpy",function () {    
    var sHTML = $(".note-editable").get(0).innerHTML;
    var vals = $("#vals").val();
    var team = window.location.pathname.substring(27,)
    // user_email = $.cookie("user_email");
    var cookies = document.cookie
    var split = cookies.split(';')
    var sub_email = split[2].substring(13,)
    user_email = sub_email.substring(0,sub_email.length-1)
    if(user_email == null ){
        alert("请先登录")
    }
    else{
        var data ={
            'user_email':user_email,
            'sHTML':sHTML,
            'team':team
        };
        $.post('/idear/teamhelpapplication/'+vals,data,function (result) {
            result =JSON.parse(result);
            if(result.status == 0){
                alert("获取信息失败")
            }else if(result.status == 1){
                alert('成功')
            }
        });
    }
});
