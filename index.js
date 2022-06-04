function onClick(){
    //1つ目の入力ボックスの値を取得する
    var value1 = document.getElementById("num1").value;
    //2つ目の入力ボックスの値を取得する
    var value2 = document.getElementById("num2").value;
    
    var min = 60 * value1;

    var sec = parseInt(min) + parseInt(value2);

    var sec_time = 42.195 * sec

    sec_time = Math.round(sec_time)

    var result = Math.floor(sec_time / 3600);
    var result2 = Math.floor(sec_time % 3600 / 60);
    var result3 = sec_time % 60;

    var ans = result + '時間' + result2 + '分' + result3 + '秒';

    document.querySelector('.result').innerHTML = ans ;

}