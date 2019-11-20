// JavaScript for Phone Application Demo Program
// Jim Skon, Kenyon College, 2017
var operation;  // operation
var editid;

$(document).ready(function () {
    $('.editdata').hide();
    $("#search-btn").click(getMatches);
    $("#add-btn").click(addEntry);
    operation = "Find Last";
    $("#clear").click(clearResults);

    $(".dropdown-menu a").click(function(){
	console.log("pick!"+$(this).text());
	if ( $(this).hasClass("main-menu") ) {
	    $(this).parents(".dropdown").find('.selection').text($(this).text());
	    operation=$(this).text();
	    console.log("Main-menu");
	    changeOperation(operation);	    
	} else if ($(this).hasClass("add-item")) {
	    $(this).parents(".dropdown").find('.selection').text($(this).text());
	    console.log($(this).text());
	} else if ($(this).hasClass("edit-item")) {
	    $(this).parents(".dropdown").find('.selection').text($(this).text());
	    console.log($(this).text());
	} 	
    });
});

changeOperation(operation);

function changeOperation(operation){
    if(operation=="Add Entry"){
	console.log("Add Entry");
	$('#addmessage').empty();
	$('.inputdata').show();
	$('.searchbox').hide();
	$('.results').hide();
	$('.editdata').hide();}
    else{
	console.log("not add entry");
	$('.editdata').hide();
	$('.inputdata').hide();
	$('.results').show();
	$('.searchbox').show();
    }    
}

// Build output table from comma delimited list
function buildTable(list) {
    //    var a = list.split(",");
    rows=JSON.parse(list);
    if (rows.length < 1) {
	return "<h3>Internal Error</h3>";
    } else if (rows.length == 1) {
	return "<h3>Nothing Found</h3>";
    } else {
	var result = '<table class="w3-table-all w3-hoverable" border="2"><tr><th>First</th><th>Last</th><th>Phone</th><th>Type</th><th>Action</th><tr>';
	for (i=0;i<rows.length;i++) {
	    row=rows[i];
	    console.log("row:",row);
	    result += "<tr><td class='first'>"+row[0]+"</td><td class='last'>"+row[1]+"</td><td class='phone'>"+row[2]+"</td><td class='type'>"+row[3]+"</td>";
	    result += "<td><button type='button' ID='"+row[4]+"' class='btn btn-primary btn-sm edit'>Edit</button> ";
	    result += "<button type='button' ID='"+row[4]+"' class='btn btn-primary btn-sm delete'>Delete</button></td></tr>";
	}
	result += "</table>";
	
	return result;
    }
}

function processEdit(){
    console.log("edit data");
    $('#searchresults').empty();
    $('.editdata').show();
    $("#edit-btn").click(editEntry);
    console.log("Edit Record: " + $(this).attr('ID'));
    var row=$(this).parents("tr");
    console.log("First name of record: "+ $(row).find('.first').text()+":"+$(row).find('.type').text());
    editid=$(this).attr('ID');

    $('#editfirst').val( $(row).find('.first').text());
    $('#editlast').val( $(row).find('.last').text());
    $('#editphone').val( $(row).find('.phone').text());
    $('#edittype').text( $(row).find('.type').text());
}

function editDone() {
    $('#editmessage').text($('#editfirst').val()+" "+$('#editlast').val()+ " SAVED");
}
function editEntry(){
    console.log("Attempting to edit an entry");
    console.log("Firstname:" + $('#editfirst').val() + "ID:" + editid);
    $('#searchresults').empty();
    $.ajax({
	url: '/cgi-bin/skon_phoneApp.py?editid='+editid +'&editfname='+$('#editfirst').val()+'&editlname='+$('#editlast').val()+'&editphone='+$('#editphone').val()+'&edittype='+$('#edittype').text()+'&operation=edit',
	dataType: 'text',
	success: editDone(),
	error: function(){alert("Error: Something went wrong");}
    });
}


function processDelete(){
    console.log("Attempting to delete an entry");
    $('#searchresults').empty();
    var id=$(this).attr('ID');
    $.ajax({
	url: '/cgi-bin/skon_phoneApp.py?deleteid='+$(this).attr('ID')+'&operation=delete',
	dataType: 'text',
	success: function(){alert("Deleted Record: " +id );},
	error: function(){alert("Error: Something went wrong");}
    });
}
function processResults(results) {
    console.log("Results:"+results);
    $('#searchresults').empty();
    $('#searchresults').append(buildTable(results));
    $(".edit").click(processEdit);
    $(".delete").click(processDelete);
}

function clearResults() {
    $('#searchresults').empty();
}

function getMatches(){
    $('.editdata').hide();
    $('#searchresults').empty();
    $.ajax({
	url: '/cgi-bin/skon_phoneApp.py?find='+$('#search').val()+'&operation='+operation,
	dataType: 'text',
	success: processResults,
	error: function(){alert("Error: Something went wrong");}
    });
}

function processAdd(results) {
    $('#addmessage').empty();
    console.log("Add:",results);
    $('#addmessage').text($('#addfirst').val()+" "+$('#addlast').val()+ " ADDED");
    $('#addfirst').val('');
    $('#addlast').val('');
    $('#addphone').val('');
    
}

function addEntry(){
    console.log("Attempting to add an entry");
    console.log("Firstname:" + $('#addfirst').val());
    $('#searchresults').empty();
    $.ajax({
	url: '/cgi-bin/skon_phoneApp.py?afname='+$('#addfirst').val()+'&alname='+$('#addlast').val()+'&aphone='+$('#addphone').val()+'&atype='+$('#addtype').text()+'&operation='+operation,
	dataType: 'text',
	success: processAdd,
	error: function(){alert("Error: Something went wrong");}
    });
}


    
