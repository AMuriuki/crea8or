function show_notifications() {
    console.log("clicked...");
    var ul_notifications = document.getElementById("ul_notifications");
    if (ul_notifications.className === "dropdown-menu dropdown-menu-media dropdown-menu-right") {
        ul_notifications.className = "dropdown-menu dropdown-menu-media dropdown-menu-right show";
    }
    else if (ul_notifications.className === "dropdown-menu dropdown-menu-media dropdown-menu-right show") {
        ul_notifications.className = "dropdown-menu dropdown-menu-media dropdown-menu-right";
    }
}

function setup() {
    document.getElementById('btn_upload').addEventListener('click', openDialog);
    function openDialog() {
        document.getElementById('uploadImage').click();
    }
}

function openUserMenu() {
    user_dropdown = document.getElementById("user_dropdown");
    if (user_dropdown.className === "dropdown-menu dropdown-menu-right pb-0") {
        user_dropdown.className = "dropdown-menu dropdown-menu-right pb-0 show";
    }
    else if (user_dropdown.className === "dropdown-menu dropdown-menu-right pb-0 show") {
        user_dropdown.className = "dropdown-menu dropdown-menu-right pb-0";
    }    
}


