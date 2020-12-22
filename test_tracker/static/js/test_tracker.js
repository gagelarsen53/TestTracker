function init_data_table() {
    $("#dashboard-table").DataTable({
        "paging": false,
        "info": false,
    });
}

function add_selected_class_to_selected_test_statuses() {
    document.querySelectorAll(".test_status").forEach(function(elem) {
        if (elem.dataset.isselected == "true") {
            elem.classList.add("test_status_selected");
        }
    });
}

function remove_selected_class_from_non_selected_test_statuses() {
    document.querySelectorAll(".test_status").forEach(function(elem) {
        if (elem.dataset.isselected != "true") {
            elem.classList.remove("test_status_selected");
        }
    });
}

function unselect_all_test_statuses() {
    document.querySelectorAll(".test_status").forEach(function(elem) {
        elem.dataset.isselected = false;
    });
}


function init_actions() {

    // Event listen for hide and show filters.
    document.getElementById("dashboard-filter-button").addEventListener("click", function() {
        element = document.getElementById("dashboard-filter-options");
        if (element.style.display == "none" || element.style.display == "") {
            element.style.display = "block";
        } else {
            element.style.display = "none";
        }

    });

    // Event listen for check and uncheck category
    document.getElementById("show-category-checkbox").addEventListener("change", function() {
        var checked = this.checked;
        categories = document.querySelectorAll(".test_category").forEach(function(elem){
            elem.style.display = checked ? "table-cell":"none"
        });
    });

    // Event listen for check and uncheck subcategory
    document.getElementById("show-subcategory-checkbox").addEventListener("change", function() {
        var checked = this.checked;
        categories = document.querySelectorAll(".test_subcategory").forEach(function(elem){
            elem.style.display = checked ? "table-cell":"none"
        });
    });

    // Event listen for selected test statuses
    document.querySelectorAll(".test_status").forEach(function(test_status){
        $(test_status).bind("click", function() {
            if (!event.ctrlKey) {
                unselect_all_test_statuses();
            }
            remove_selected_class_from_non_selected_test_statuses();
            this.dataset.isselected = true;
            add_selected_class_to_selected_test_statuses();
        });
    });

    // Event listen to deselect table cells
    document.addEventListener('click', function(e) {
        if (!$(e.target).hasClass("test_status")) {
            unselect_all_test_statuses();
            remove_selected_class_from_non_selected_test_statuses();
        }
    });
}

$(document).ready(function(){
    init_actions();
    init_data_table();
});