const API = 'https://randomuser.me/api/'

async function getUser(){
    const response = await fetch(API);
    var data = await response.json();
    if(data){
        console.log('hello');
        console.log(data);
        get_required_data(data);
    }
}
function get_required_data(data){
    var name = data.results[0].name.first + " " + data.results[0].name.last;
    var title = data.results[0].name.title;
    var email = data.results[0].email;
    var age = data.results[0].dob.age;
    var image = data.results[0].picture.large;
    var address = data.results[0].location.street.name + " " + data.results[0].location.street.number + ', ' + data.results[0].location.city + ', ' + data.results[0].location.state + ', ' + data.results[0].location.country;
    var phone = data.results[0].phone;
    var cell = data.results[0].cell;
    var required_data =  {'title':title, 'name':name, 'email':email, 'age':age, 'image':image, 'address':address, 'phone':phone, 'cell':cell};
    put_data(required_data);
}
function put_data(data){
    console.log(data);
    document.getElementById('name').innerHTML = data.name;
    document.getElementById('title').innerHTML = data.title;
    document.getElementById('email').innerHTML = data.email;
    document.getElementById('age').innerHTML = data.age;
    document.getElementById('image').src = data.image;
    document.getElementById('address').innerHTML = data.address;
    document.getElementById('phone').innerHTML = data.phone;
    document.getElementById('cell').innerHTML = data.cell;
}
getUser();