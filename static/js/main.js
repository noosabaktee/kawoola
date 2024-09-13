$('#loading').hide();
$('#content').show();
// $(function(){
//   AOS.init({
//     offset: 50,
//     once: true,
//     duration: 1200
//   });
// })
window.jsPDF = window.jspdf.jsPDF;

$('.to-pdf').click(function(){
  $(this).hide()
  html2canvas( document.querySelector("#content"), { logging: true, letterRendering: 1, allowTaint: false,  useCORS: true } ).then(canvas => { 
    var a = document.createElement('a');
    img = canvas.toDataURL("image/jpeg").replace("image/jpeg", "image/octet-stream");
    var doc = new jsPDF('l', 'px', [$("body").width(),$("body").height()]);
    doc.addImage(img, 'JPEG', 0, 0,$("body").width(), $("body").height());
    doc.save($(this).attr("name") + ".pdf");
    $('.to-pdf').show()
  })
  
})

$('.show-hide-pw').click(function(){
    var x = $('input[name="password1"]');
    if (x.attr('type') == 'password') {
        x.attr('type', 'text');
    }else{
        x.attr('type', 'password');
    }
})

let bg1 = $('body').attr('bg1');
let text1 = $('body').attr('text1');

let bg2 = $('body').attr('bg2');
let text2 = $('body').attr('text2');

window.onload = function () {
   var svg = document.querySelectorAll("object");
   Array.from(svg).forEach((element, index) => {
    // conditional logic here.. access element
    $(element).css('marginBottom', '-5px')
    // Get the SVG document inside the Object tag
    var svgDoc = element.contentDocument;
    // Get one of the SVG items by ID;
    if ($('#riwayat-3').length > 0) {
      text1 = text2
    }
    svgDoc.querySelector("path").style.fill = text1
    svg = svgDoc.querySelector("svg")
    imgElement = $(element).parent().find('span')
    imgElement.html(svg)
    $(element).remove()
  });
}

if ($('#riwayat-3').length > 0) {
  $('.bg-1').css({'background-color':bg1,'color':text1});
  $('body').css({'background-color':bg2,'color':text2});
  $('h4').css({'background-color':bg1,'color':text1});
}else{ 
  $('#left').css({'background-color':bg1,'color':text1});
  $('#right').css({'background-color':bg2,'color':text2});
}

if ($('#riwayat-2').length > 0) {
  $('#left').find('h4').css({'background-color':bg2,'color':text2});
  $('#right').find('h4').css({'background-color':bg1,'color':text1});
}


$('head').append(`<style>
  ul.timeline:before{
    background: `+ text1 +`;
  }
  ul.timeline > li:before{
    background: `+ bg1 +`;
    border: 3px solid `+ text1 +`;
  }
  ul.list-skill li:before {
    background-color: `+ text2 +`;
  }
  ul.experience-list > li:before {
    background-color: `+ text2 +`;
  }
  </style>`);
$('hr').css('border-top', '3px solid ' + text2)

$(".navigation").hide();

$(document).scroll(function() { 

  if($(window).scrollTop() >= 80) {
    $(".navigation").show();
  }else{
    $(".navigation").hide();
  }
});

function clean(x) {
  x.value = x.value.replace(/\s/g, "");
  x.value = x.value.replace(/\@/g, "");
  x.value = x.value.replace(/\!/g, "");
  x.value = x.value.replace(/\#/g, "");
  x.value = x.value.replace(/\$/g, "");
  x.value = x.value.replace(/\%/g, "");
  x.value = x.value.replace(/\^/g, "");
  x.value = x.value.replace(/\&/g, "");
  x.value = x.value.replace(/\*/g, "");
  x.value = x.value.replace(/\(/g, "");
  x.value = x.value.replace(/\)/g, "");
  x.value = x.value.replace(/\-/g, "");
  x.value = x.value.replace(/\=/g, "");
  x.value = x.value.replace(/\+/g, "");
  x.value = x.value.replace(/\\/g, "");
  x.value = x.value.replace(/\|/g, "");
  x.value = x.value.replace(/\{/g, "");
  x.value = x.value.replace(/\}/g, "");
  x.value = x.value.replace(/\[/g, "");
  x.value = x.value.replace(/\]/g, "");
  x.value = x.value.replace(/\:/g, "");
  x.value = x.value.replace(/\;/g, "");
  x.value = x.value.replace(/\"/g, "");
  x.value = x.value.replace(/\'/g, "");
  x.value = x.value.replace(/\</g, "");
  x.value = x.value.replace(/\>/g, "");
  x.value = x.value.replace(/\,/g, "");
  x.value = x.value.replace(/\./g, "");
  x.value = x.value.replace(/\//g, "");
  x.value = x.value.replace(/\?/g, "");
  x.value = x.value.toLowerCase();
}

$('input[name="username"]').keyup(function(){
   clean(this);
})

$('.color-picker').spectrum({
  type: "text",
  showAlpha: false
});

// Change color templates
$('#bg-1').change(function(){
    $('#color-1').css('backgroundColor', $(this).val())
})
$('#text-1').change(function(){
    $('#color-1').find('span').css('color', $(this).val())
})

$('#bg-2').change(function(){
    $('#color-2').css('backgroundColor', $(this).val())
})
$('#text-2').change(function(){
    $('#color-2').find('span').css('color', $(this).val())
})

$('input, textarea').keyup(function() {
    if($(this).val().length == 1){
        $(this).val($(this).val().trim())
    }
});

$('.btn-edu').click(function(){
    parent = $(this).parent().parent()
    i = parent.find('.instansi').html()
    a = parent.find('.awal').html()
    ak = parent.find('.akhir').html()
    l = parent.find('.jurusan').html()
    e = $('#form-edu')
    e.find('#instansi').val(i)
    e.find('#awal').val(a)
    e.find('#akhir').val(ak)
    e.find('#jurusan').val(l)
    e.attr('action', e.attr('update'))
    e.find('button').html("Edit")
    index = $(this).attr('index')
    new_element = '<input type="hidden" name="index" value="'+index+'" />'
    e.append(new_element)
})

$('.add-edu').click(function(){
  parent = $(this).parent().parent()
  e = $('#form-edu')
  e.find('#instansi').val("")
  e.find('#awal').val("")
  e.find('#akhir').val("")
  e.find('#jurusan').val("")
  e.attr('action', e.attr('create'))
  e.find('button').html("Add")
})

$('.btn-ach').click(function(){
    parent = $(this).parent().parent()
    p = parent.find('.prestasi').html()
    t = parent.find('.tahun').html()
    tpt = parent.find('.tempat').html()
    e = $('#form-ach')
    e.find('#prestasi').val(p)
    e.find('#tahun').val(t)
    e.find('#tempat').val(tpt)
    e.attr('action', e.attr('update'))
    e.find('button').html("Edit")
    index = $(this).attr('index')
    new_element = '<input type="hidden" name="index" value="'+index+'" />'
    e.append(new_element)
})

$('.add-ach').click(function(){
  e = $('#form-ach')
  e.find('#prestasi').val("")
  e.find('#tahun').val("")
  e.find('#tempat').val("")
  e.attr('action', e.attr('create'))
  e.find('button').html("Add")
})

$('.btn-exp').click(function(){
    parent = $(this).parent().parent()
    exp = parent.find('.experience').html()
    t = parent.find('.tahun').html()
    tpt = parent.find('.tempat').html()
    sum = parent.find('.summary').html()
    e = $('#form-exp')
    e.find('#experience').val(exp)
    e.find('#tahun').val(t)
    e.find('#tempat').val(tpt)
    e.find('#summary').val(sum)
    e.attr('action', e.attr('update'))
    e.find('button').html("Edit")
    index = $(this).attr('index')
    new_element = '<input type="hidden" name="index" value="'+index+'" />'
    e.append(new_element)
})

$('.add-exp').click(function(){
  e = $('#form-exp')
  e.find('#experience').val("")
  e.find('#tahun').val("")
  e.find('#tempat').val("")
  e.find('#summary').val("")
  e.attr('action', e.attr('create'))
  e.find('button').html("Add")
})

$('.btn-skill').click(function(){
    parent = $(this).parent().parent()
    s = parent.find('.skill').html()
    l = parent.find('.level').html()
    e = $('#form-skill')
    e.find('#skill').val(s)
    e.find('#level').val(l)
    e.attr('action', e.attr('update'))
    e.find('button').html("Edit")
    index = $(this).attr('index')
    new_element = '<input type="hidden" name="index" value="'+index+'" />'
    e.append(new_element)
})

$('.add-skill').click(function(){
  e = $('#form-skill')
  e.find('#skill').val("")
  e.find('#level').val("")
  e.attr('action', e.attr('create'))
  e.find('button').html("Add")
})

function PreviewImage() {
    alert($("#photo"))
}

function readURL(input) {
    var file = input.files[0];
    var fileType = file["type"];
    var validImageTypes = ["image/jpeg", "image/png"];
    if ($.inArray(fileType, validImageTypes) < 0) {
         alert("File harus berupa gambar")
         return false
    } else if (file.size > 2000000){
        alert("Gambar tidak boleh lebih dari 2 MB")
         return false
    }
  
    if (input.files && input.files[0]) {
        $('#preview-photo').show();
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#preview-photo').attr('src', e.target.result);
        }

        reader.readAsDataURL(file);
    }
}

$('.edit-photo-btn').hide()
$("#photo").change(function(){
    readURL(this);
    $('.edit-photo-btn').show()
});

autosize($('textarea'));
