function addnumbers(){
    const num3 = document.getElementById("num1").value
    const num4 = document.getElementById("num2").value
    const num5 = Number(num3) + Number(num4)
    document.getElementById("p1").textContent = "sum"+ num5
}