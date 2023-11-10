var viloyat = document.getElementById('viloyat')

function viloyatTopish() {
    var value = viloyat.value
    var text = viloyat.options[viloyat.selectedIndex].text
    console.log(value, text)
}
viloyat.onchange = viloyatTopish;
viloyatTopish()

var tuman = document.getElementById('tuman')


