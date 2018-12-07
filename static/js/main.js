
$(function () {

    for(var i =1960;i <2040;i ++){
        $("#year").append('<option value="' +i +'">' +i +'</option>');
    }

    for(var j =1;j <13;j ++){
        $("#month").append('<option value="' +j +'">' +j +'</option>');
    }

    for(var k =1;k <32;k ++){
        $("#day").append('<option value="' +k +'">' +k +'</option>');
    }


    setTimeout("showT1()",0);
    setTimeout("showFT2()",500);
    setTimeout("showT3()",1000);
    setTimeout("showT4()",1500);
    setTimeout("showFT3()",2000);

    setTimeout("showSPE()",0);

    setTimeout("showFT1()",500);


});

function showT1() {
    $("#main >p:first-child").children("span").eq(0).css("top","58px");
    $("#main >p:first-child").children("span").eq(0).css("left","150px");
}

function showT3() {
    $(".tips3").css("top","160px");
    $(".tips3").css("right","10px");
}

function showT4() {
    $(".tips4").css("top","240px");
    $(".tips4").css("right","10px");
}

function showFT1(){
    $(".tips").css("top","436px");
    $(".tips").css("right","120px");
}

function showFT2() {
    $("#filter >ul >li").eq(2).css("top","10px");
    $("#filter >ul >li").eq(2).css("left","180px");
}

function showFT3() {
    $(".tips5").css("bottom","5px");
    $(".tips5").css("left","60px");
}

function showSPE() {
    $(".spetip").css("top","84px");
    $(".spetip").css("left","138px");
}
