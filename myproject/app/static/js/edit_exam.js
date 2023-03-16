

// Add New choice
intital_value = 1
$(".add_exam_field").click(function(){

$("#append_inital_field").append(

    ` <tr class="init_remove`+intital_value+`">
            <td>
                <input type="text" placeholder="Title" name="initial_label`+intital_value+`" id="" class="intial-text">
                <input type="hidden" class="initial_count" name="initial_count" value='`+intital_value+`'>
            </td>

            <td>
                <div  class="input-group">
                    <input type="checkbox"  name="unique`+intital_value+`" value="True" class="intial-text">
                </div>
            </td>

            <td>
                <select class="intial-text2" name="initial_type`+intital_value+`">
                    <option value="Text Input" selected>Text Input</option>
                    <option value="selection">Selection</option>
                    <option value="Date Field">Date Field</option>
                </select>         
            </td>

            <td id='multiple_choice`+intital_value+`'>
                <a href="#" style="font-size: 16px;float:right;
            color: black;"  onclick="multiple_choice_add(`+intital_value+`)">+</a>
                
            </td>

            <td> 
            <div class="action-tbl d-flex justify-content-end">
                    
                <i style="cursor: pointer;" class="fa fa-trash-o mx-1 " data-toggle="tooltip"
                data-placement="top" title="" data-original-title="Delete"  onclick="initial_field_remove(`+intital_value+`)" ></i>
            
            </div>
            </td>

        </tr>`                       
        
)

intital_value = intital_value + 1
});


function multiple_choice_add(val){
    $("#multiple_choice"+val).append(
        `<input class="intial-text" placeholder="Type your option" type="text" name="initial_answer`+val+`"><br><br>`
    )
}



function initial_field_remove(val)
{
var tr_id = val
$('.init_remove'+tr_id).hide()
div_update = document.getElementsByClassName("init_remove"+tr_id).innerHTML = "";
$('.init_remove'+tr_id).empty()
}

//Add choice over



// section updated

$(document).on("click", ".title_edit", function () {
    var myid = $(this).attr("data-id") ;
    var title = $(this).attr("data-title") ;
    $("#title_updated_id").val(myid)
    $("#title_name_update").val(title)
});



//survey time limit
$("#time_limit").click(function () {
    exam_check = $("#time_limit").is(":checked")
    if (exam_check == true) {
        $("#show_timelimit").show();
    } else {
        $("#show_timelimit").hide();
        $("#exam_time_limit").val(" ");
    }
});


// access mode display 
$("#select_access_mode").change(function () {
    select_value = $("#select_access_mode").val();
    if (select_value == 1) {
        $("#attemp_lim").show()
    } else {
        $("#attemp_lim").hide()
    }
})


// login reqiured
$("#login_required").click(function () {
    login_required = $("#login_required").is(":checked")
    if (login_required == true) {
        $("#attemp_lim").show()
    } else {
        $("#attemp_lim").hide()
    }
});



// scetion delete functionality
function section_question_delete_btn(id) {
    var url = "delete_question_section";
    $.ajax({
        url: url,
        data: {
            'id': id
        },
        success: function (data) {
            $("#delete_initial_field_div").html(data);
            $('#delete_initial_field_modal').modal('show');
        }
    });
}




// Question view on click 
function section_Question_view(data_id){
    var data_id = data_id
    var modal_name = data_id+"-"+data_id

    var isClassExist = document.getElementsByClassName('question-modal-'+modal_name);
    if (isClassExist.length > 0) {
        $('.question-modal-'+modal_name).modal('show');
        }

    else{

    $.ajax({
            type: "GET",
            url: "section_Question_view_modal",
            data: {
                data_id: data_id,
                modal_id:data_id
                
            },
            success: function (data) {
                var modal_name = data_id+"-"+data_id
                $(".section_Question_view_modal").append(data);
                $('.question-modal-'+modal_name).modal('show');
            }
        })
    }
    }



