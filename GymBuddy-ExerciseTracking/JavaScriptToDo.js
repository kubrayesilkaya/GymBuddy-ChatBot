// Get the To-Do list
const myUL = document.getElementById("myUL");

// Get the items in the To-Do list
let itemsArray = localStorage.getItem('items') ? JSON.parse(localStorage.getItem('items')) : [];

// Add the existing items to the To-Do list
for (let i = 0; i < itemsArray.length; i++) {
    createListElement(itemsArray[i].text, itemsArray[i].checked);
}

// Add a new item to the To-Do list and save it to local storage
function newElement() {
    let inputValue = document.getElementById("myInput").value;
    if (inputValue === '') {
        alert("You must write something!");
    } else {
        let item = { text: inputValue, checked: false };
        itemsArray.push(item);
        localStorage.setItem('items', JSON.stringify(itemsArray));
        createListElement(inputValue, false);
    }
}

// Remove an item from the To-Do list and from local storage
function removeElement(e) {
    let index = itemsArray.findIndex(item => item.text === e.target.parentElement.innerText);
    itemsArray.splice(index, 1);
    localStorage.setItem('items', JSON.stringify(itemsArray));
    e.target.parentElement.remove();
}

// Create a new list element and append it to the To-Do list
function createListElement(text, checked) {
    let li = document.createElement("li");
    li.innerText = text;
    li.setAttribute("data-id", itemsArray.length - 1);

    if (checked) {
        li.classList.add("checked");
    }

    li.addEventListener("click", function () {
        li.classList.toggle("checked");
        itemsArray[li.getAttribute("data-id")].checked = li.classList.contains("checked");
        localStorage.setItem("items", JSON.stringify(itemsArray));
    });

    let span = document.createElement("span");
    span.className = "close";
    span.innerText = "\u00D7";
    span.addEventListener("click", removeElement);

    li.appendChild(span);
    myUL.appendChild(li);
}