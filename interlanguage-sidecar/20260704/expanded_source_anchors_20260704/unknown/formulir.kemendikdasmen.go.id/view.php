<!DOCTYPE html>
<html lang="en" >
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>FORMULIR PERMOHONAN INFORMASI PUBLIK</title>
<base href="https://formulir.kemendikdasmen.go.id/" />
<link rel="stylesheet" type="text/css" href="./data/form_1035451/css/view.css?b9aacd" media="all" />
<link rel="stylesheet" type="text/css" href="view.mobile.css?b9aacd" media="all" />
<link rel="stylesheet" type="text/css" href="./data/themes/theme_284.css" media="all" />

<script type="text/javascript" src="js/jquery.min.js?b9aacd"></script>
<script type="text/javascript" src="view.js?b9aacd"></script>

<script type="text/javascript" src="js/uploadifive/jquery.uploadifive.js"></script>


<script type="text/javascript" src="js/signature_pad/signature_pad.umd.js"></script>






</head>
<body id="main_body" class="">
	
	<div id="form_container" class="">
		<h1><a>FORMULIR PERMOHONAN INFORMASI PUBLIK</a></h1>
		<form id="form_1035451" class="appnitro top_label"  method="post" data-highlightcolor="#adddeb" action="/view.php">
					<div class="form_description">
			<h2>FORMULIR PERMOHONAN INFORMASI PUBLIK</h2>
			<p>Formulir permohonan informasi secara daring ini merupakan hak untuk memperoleh informasi publik sesuai Umdang-Undang No 14 Tahun 2008 Tentang Keterbukaan Informasi Publik</p>
		</div>						
			<ul >
			
			
			
					<li id="li_1"  >
		<label class="description" for="element_1">Nama Lengkap <span id="required_1" aria-hidden="true" class="required">*</span></label>
		<div>
			<input id="element_1" name="element_1"   aria-required="true"  class="element text medium" type="text" value=""   />
			 
		</div> 
		</li>		<li id="li_2"  >
		<label class="description" for="element_2">Nomor Telepon <span id="required_2" aria-hidden="true" class="required">*</span></label>
		<div>
			<input id="element_2" name="element_2"   aria-required="true"  class="element text medium" type="text" value=""   />
			 
		</div> 
		</li>		<li id="li_3"  >
		<label class="description" for="element_3">Pos-el <span id="required_3" aria-hidden="true" class="required">*</span></label>
		<div>
			<input id="element_3" name="element_3"   aria-required="true" class="element text medium" type="text" maxlength="255" value="" /> 
		</div> 
		</li>
				<li id="li_4"  >
		<label class="description" for="element_4">Alamat <span id="required_4" aria-hidden="true" class="required">*</span></label>
		<div>
			<textarea id="element_4" name="element_4"   aria-required="true" class="element textarea small" rows="8" cols="90" ></textarea>
			 
		</div> 
		</li>		<li id="li_5"  >
		<label class="description" for="element_5">Nomor Identitas (KTP/SIM/KTM) <span id="required_5" aria-hidden="true" class="required">*</span></label>
		<div>
			<input id="element_5" name="element_5"   aria-required="true"  class="element text medium" type="text" value=""   />
			 
		</div> 
		</li>		<li id="li_6"  >
		<label for="element_6" class="description" for="element_6">Lampiran Tanda Pengenal <span id="required_6" aria-hidden="true" class="required">*</span></label>
		<div>
			<input id="element_6" name="element_6" class="element file" type="file"  />
			<div id="element_6_queue" class="file_queue"></div> 
			<script type="text/javascript">
	$(function(){
		 if(is_support_html5_uploader()){
		 	$('#element_6').uploadifive({
		 		'uploadScript'     : 'upload.php',
		 		'buttonText'	   : 'Select Files',
		 		'removeCompleted' : false,
				'formData'         : {
									  'form_id': 1035451,
				        			  'element_id': 6,
				        			  'file_token': '749605584928d4f0677b0e99f8c05681'
				                     },
				'auto'             : true,
				'multi'       	   : true,
				'queueSizeLimit' : 5,
				'fileSizeLimit'  : '5MB',
				'queueID'          : 'element_6_queue',
				'onAddQueueItem' : function(file) {
		            var file_type_limit_exts = 'jpg,jpeg,png,gif,bmp,pdf';
		            var file_type_limit_exts_array = file_type_limit_exts.split(',');

		            var uploaded_file_ext 	 = file.name.split('.').pop().toLowerCase();
		            
		            var file_exist_in_array = false;
		            $.each(file_type_limit_exts_array,function(index,value){
		            	if(value == uploaded_file_ext){
		            		file_exist_in_array = true;
		            	}
		            });
					if(file_type_limit_exts.trim().length > 0){
			            if(file_exist_in_array == false){
			            	$("#" + file.queueItem.attr('id')).addClass('error');
				            $("#" + file.queueItem.attr('id') + ' span.fileinfo').text(" - Error. This file type is not allowed.");
			            }
		        	}

		            
		            if($("html").hasClass("embed")){
				    	$.postMessage({mf_iframe_height: $('body').outerHeight(true)}, '*', parent );
				   	}
		        },
				'onUploadComplete' : function(file, response) { 
					

					var is_valid_response = false;
					try{
						var response_json = JSON.parse(response);
						is_valid_response = true;
					}catch(e){
						is_valid_response = false;
						alert(response);
					}
					var queue_item_id =  file.queueItem.attr('id');
					
					if(is_valid_response == true && response_json.status == "ok"){
						var remove_link = "<a class=\"close\" href=\"javascript:remove_attachment('" + response_json.message + "',1035451,6,'" + queue_item_id + "',0,'749605584928d4f0677b0e99f8c05681');\"><img border=\"0\" src=\"images/icons/delete.png\" /></a>";
						
						$("#" + queue_item_id + " a.close").replaceWith(remove_link);
				        $("#" + queue_item_id + ' span.filename').prepend('<img align="absmiddle" class="file_attached" src="images/icons/attach.gif">'); 
			        }else{
			        	$("#" + queue_item_id).addClass('error');
			        	$("#" + queue_item_id + " a.close").replaceWith('<img style="float: right" border="0" src="images/icons/exclamation.png" />');
						$("#" + queue_item_id + " span.fileinfo").text(" - Error! Unable to upload");
					}

					if($("html").hasClass("embed")){
				    	$.postMessage({mf_iframe_height: $('body').outerHeight(true)}, '*', parent );
				   	} 

					if($("#form_1035451").data('form_submitting') === true){
				       	upload_all_files();
					}
				}
			});
			$("#element_6_upload_link").remove();
		 }else{
	     	$("#element_6_token").remove();
		 }
    });
</script>
<input type="hidden" id="element_6_token" name="element_6_token" value="749605584928d4f0677b0e99f8c05681" />
<a id="element_6_upload_link_uploadifive" style="display: none" href="javascript:$('#element_6').uploadifive('upload');">Attach Files</a>
		</div> <p class="guidelines" id="guide_6"><small>Format fail jpg, jpeg, png, gif, bmp, pdf maksimal 5 MB</small></p> 
		</li>		<li id="li_7"  >
		<label class="description" for="element_7">Rincian Informasi yang Dibutuhkan <span id="required_7" aria-hidden="true" class="required">*</span></label>
		<div>
			<textarea id="element_7" name="element_7"   aria-required="true" class="element textarea medium" rows="8" cols="90" ></textarea>
			 
		</div> 
		</li>		<li id="li_8"  >
		<label class="description" for="element_8">Tujuan Penggunaan Informasi <span id="required_8" aria-hidden="true" class="required">*</span></label>
		<div>
			<textarea id="element_8" name="element_8"   aria-required="true" class="element textarea medium" rows="8" cols="90" ></textarea>
			 
		</div> 
		</li>		<li id="li_9"   class="dropdown">
		<label class="description" for="element_9">Bentuk informasi yang diminta <span id="required_9" aria-hidden="true" class="required">*</span></label>
		<div>
		<select class="element select medium" aria-required="true" id="element_9" name="element_9"> 
			<option value="" selected="selected"></option>
<option value="1"  >Melihat/membaca/mendengarkan/mencatat</option>
<option value="2"  >Mendapatkan salinan informasi (salinan lunak)</option>
<option value="3"  >Mendapatkan salinan informasi (salinan keras))</option>

		</select>
		</div> 
		</li>		<li id="li_10"   class="dropdown">
		<label class="description" for="element_10">Cara mendapatkan salinan informasi <span id="required_10" aria-hidden="true" class="required">*</span></label>
		<div>
		<select class="element select medium" aria-required="true" id="element_10" name="element_10"> 
			<option value="" selected="selected"></option>
<option value="1"  >Mengambil Langsung</option>
<option value="2"  >Kurir</option>
<option value="3"  >Pos</option>
<option value="4"  >Faksimili</option>
<option value="5"  >Pos-el</option>

		</select>
		</div> 
		</li>		<li id="li_11"  class="signature">
		<label class="description" for="element_11">Pemohon Informasi, <span id="required_11" aria-hidden="true" class="required">*</span></label>
		<div id="mf_signature_pad_11">
						<div class="mf_signature_switch" style="text-align: right">
				<a class="sig_switch_draw active" href="javascript: switch_signature_type(11,'draw');">Draw</a> or 
				<a class="sig_switch_type " href="javascript: switch_signature_type(11,'type');">Type</a>
			</div>
	        <div class="mf_signature_draw" style="display: block">
		        <div class="mf_signature_wrapper medium" style="height: 150px">
		          <canvas id="mf_canvas_signature_pad_11" class="mf_canvas_signature_pad" style="width: 100%; height: 100%"></canvas>
		        </div>
		        <span class="label">Saya mengerti ini adalah representasi hukum dari tanda tangan saya</span>
		        <a class="mf_signature_clear element_11_clear" href="javascript:clear_signature(11)">Clear</a>
	        </div>
	        <div class="mf_signature_type" style="display: none">
	        	<label class="description" for="element_11_text_signature">Full Name</label>
				<input id="element_11_text_signature" name="element_11_text_signature" data-elementid="11" class="element text large text_signature" type="text" value="" />
				<div class="mf_signature_wrapper medium" style="height: 100px;margin-top: 20px">
					<img id="element_11_text_signature_img" src="signature_img_renderer.php" style="height: 75px;margin-top: 10px;margin-left: 15px"/>	 
				</div> 
				<span class="label">Saya mengerti ini adalah representasi hukum dari tanda tangan saya</span>
	        </div>
	        <input type="hidden" name="element_11" id="element_11" value="">
	        <script type="text/javascript">	   
				var canvas_11 = document.getElementById('mf_canvas_signature_pad_11');
				var signature_pad_11 = new SignaturePad(canvas_11);

				signature_pad_11.onEnd = function(){
					$("#element_" + 11).val(signature_pad_11.toDataURL());
				};
				refresh_signature(signature_pad_11,canvas_11);
				
			</script> 
		</div> 
		</li>
			
			
			
					<li id="li_buttons" class="buttons">
			    <input type="hidden" name="form_id" value="1035451" />
			    
			    <input type="hidden" id="mfsid" name="mfsid" value="vjqm8a9d4h7mtfio5sg9k368v1" />
			    
			    
			    <input type="hidden" name="submit_form" value="1" />
			    <input type="hidden" name="page_number" value="1" />
				<input id="submit_form" class="button_text" type="submit" name="submit_form" value="Simpan" />
		</li>
			</ul>
		</form>	
		<div id="footer">
			
		</div>
	</div>
	
	</body>
</html>