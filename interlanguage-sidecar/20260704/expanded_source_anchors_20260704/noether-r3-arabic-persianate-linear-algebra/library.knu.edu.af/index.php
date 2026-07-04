﻿
<!doctype html>
<html dir="rtl" lang="ar">
  <head>    
    <meta charset='utf-8'>

	<meta name="keywords" content="" />
	<meta name="description" content="دسترسی همگانی(OPAC) کتابخانه دانشگاه خاتم النبیین (ص)." />

	<meta name="robots" content="all" />
	<!--IE compatibility-->
	<meta http-equiv='X-UA-Compatible' content='IE=8'/>

	<script src='includes/javascript/jquery.js' type='text/javascript'></script>
	
	
	<title>دسترسی همگانی(OPAC) کتابخانه دانشگاه خاتم النبیین (ص)</title>		
	
	<link rel='stylesheet' type='text/css' href='./includes/javascript/bootstrap-4.6.1-plus-rtl-rev.1-dist/css/bootstrap-rtl.min.css' />
	<link rel='stylesheet' type='text/css' href='./includes/javascript/bootstrap-4.6.1-plus-rtl-rev.1-dist/css/bs_icon/bootstrap-icons.css' />

	
	<script src='./includes/javascript/bootstrap-4.6.1-plus-rtl-rev.1-dist/js/bootstrap.min.js'></script>
	<script src='./includes/javascript/bootstrap-4.6.1-plus-rtl-rev.1-dist/js/bootstrap.bundle.min.js'></script>
	
	
	<script type='text/javascript'>$(function () {
		$('[data-toggle="tooltip"]').tooltip()})
	</script>
	
	
	<link rel='stylesheet' type='text/css' href='./styles/app34/columns.css' />
	<link rel='stylesheet' type='text/css' href='./styles/app34/crsl.css' />
	<link rel='stylesheet' type='text/css' href='./styles/app34/tags.css' />
	<link rel='stylesheet' type='text/css' href='./styles/app34/main.css' />
	<link rel='stylesheet' type='text/css' href='./styles/app34/print.css' />
	<link rel='stylesheet' type='text/css' href='./styles/app34/viewer.css' />
	<link rel='stylesheet' type='text/css' href='./styles/app34/ext_search.css' />
	<link rel='stylesheet' type='text/css' href='./styles/app34/perd_iss_lst.css' />
	<link rel='stylesheet' type='text/css' href='./styles/app34/bask.css' />
	<link rel='stylesheet' type='text/css' href='./styles/app34/slider_style.css' />
	<link rel='stylesheet' type='text/css' href='./styles/app34/photo_gallery.css' /><!-- css_authentication -->
	<link href='./images/favicon.ico' rel='shortcut icon' type='image/x-icon' />
	<script type="text/javascript" src="includes/javascript/drag_n_drop.js"></script>
	<script type="text/javascript" src="includes/javascript/handle_drop.js"></script>
	<script type="text/javascript" src="includes/javascript/popup.js"></script>
	<script type="text/javascript" src="includes/javascript/select.js"></script><script type='text/javascript' src='./includes/javascript/http_request.js'></script></head><body onload="window.defaultStatus='دسترسی همگانی';"  id="appopac">
		<script type='text/javascript'>
		function show_what(What, id) {
			var whichISBD = document.getElementById('div_isbd' + id);
			var whichPUBLIC = document.getElementById('div_public' + id);
			var whichtabISBD = document.getElementById('tab_isbd' + id);
			var whichtabPUBLIC = document.getElementById('tab_public' + id);
			
			var whichCOPY = document.getElementById('div_copy' + id);	
			var whichCOPY_LOC = document.getElementById('div_copy_loc' + id);	
			var whichtabCOPY = document.getElementById('tab_copy' + id);
			var whichtabCOPY_LOC = document.getElementById('tab_copy_loc' + id);
			if (What == 'ISBD') {
				whichISBD.style.display  = 'block';
				whichPUBLIC.style.display = 'none';
				whichtabPUBLIC.className = 'isbd_public_inactive';
				whichtabISBD.className = 'isbd_public_active';
			}else if(What == 'COPY_LOC') {
				whichCOPY_LOC.style.display = 'block';
				whichCOPY.style.display = 'none';		
				whichtabCOPY.className = 'isbd_public_inactive';		
				whichtabCOPY_LOC.className = 'isbd_public_active';
			}else if(What == 'COPY') {
				whichCOPY_LOC.style.display = 'none';
				whichCOPY.style.display = 'block';
				whichtabCOPY.className = 'isbd_public_active';
				whichtabCOPY_LOC.className = 'isbd_public_inactive';
			} else {
				whichISBD.style.display = 'none';
				whichPUBLIC.style.display = 'block';
				whichtabPUBLIC.className = 'isbd_public_active';
				whichtabISBD.className = 'isbd_public_inactive';
			}
			
		}
		</script><script type='text/javascript' src='./includes/javascript/tablist_ajax.js'></script>
	<script type='text/javascript' src='./includes/javascript/tablist.js'></script>
	<script type='text/javascript' src='./includes/javascript/http_request.js'></script>
	<div id='att' style='z-Index:1000'></div>
	<header class='d-flex flex-wrap justify-content-between align-items-center border-bottom' style='margin-top: -20px;'>
		<div class='col-sm-10'>
			<a href='./'><img class='navbar-brand' src='images/book_search.png' alt='لوگو' ></a>
		</div>
		<div class='col-sm-2'>
			شنبه ۱۳ سَرَطان ۱۴۰۵
		</div>
	</header>		
	
	<div class='navbar-container'>
		<nav class='navbar navbar-expand-lg navbar-light bg-light border-bottom'>
			<button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarToggler1' aria-controls='navbarToggler1' aria-expanded='false' aria-label='Toggle navigation'>
				<span class='navbar-toggler-icon'></span>
			</button>
			<div class='collapse navbar-collapse' id='navbarToggler1'> 				
				<div class='col-sm-8'>
					<ul class='navbar-nav me-auto mb-2 mb-sm-0'><li class='nav-item nav_bg shadow rounded'><a class='nav-link' href="./index.php?lvl=index" class=''><span class='bi bi-house-fill'></span>&nbsp;<span>صفحه اصلی</span></a></li>
<li class='nav-item nav_bg shadow rounded'><a class='nav-link' href="index.php?lvl=last_records" class='actions_history'><span class='bi bi-book'>&nbsp;</span><span>تازه‌های کتابخانه</span></a></li>
<li class='nav-item nav_bg shadow rounded'><a class='nav-link' href="./index.php?lvl=info_pages&page_id=2" ><span>راهنما</span></a></li>
  <li class='nav-item nav_bg shadow rounded dropdown'>
	<a class='nav-link dropdown-toggle' href='#' id='navbarDropdown' role='button' data-toggle='dropdown' aria-expanded='false'>
	  <span class='bi bi-people'>&nbsp;</span>ورود به سیستم
	</a>
	<div class='dropdown-menu' aria-labelledby='navbarDropdown' style='width: 300px;'>
		<div class='row'>
			<div class='col-md-12'>					
				<form class='form' id='signin' action='borrower.php' method='post' name='myform'>
					<div class='form-group'>
						 <label class='sr-only' for='exampleInputEmail2'>کدکاربری</label>
						 <input type='text' name='login' class='form-control' placeholder='کدکاربری' required=''>
					</div>
					<div class='form-group'>
						 <label class='sr-only' for='exampleInputPassword2'>Password</label>
						 <input type='password' name='password' class='form-control' placeholder='کلمه عبور' required=''>
						 <p><a class='text-primary text-decoration-none small' href=./subscribe.php>درخواست عضویت</a></p>
						 <p><a class='text-primary text-decoration-none small' href=./askmdp.php>کلمه عبورتان را فراموش کرده‌اید؟</a></p>
					</div>
					<div class='form-group'>
						 <button type='submit' class='btn btn-primary btn-block'>تایید</button>
					</div>					
				</form>
			</div>
			
		</div>
	</div>
</li> </ul>	
				</div>
				<div class='col-sm-4' style='padding-right:34px;padding-left: 34px;'>
					<form class='form-inline my-2 my-lg-0' name='search_input' action='./index.php?lvl=m_rslt&auto_lvl1=1' method='post' onSubmit="if (search_input.user_query.value.length == 0) { search_input.user_query.value='*'; return true; }" style='height:38px'>
<input type='hidden' name='high_lights' value='!!high_lights!!'/>
            <div class='input-group mb-3 shadow'> <select data-toggle='tooltip' title='نام پایگاه' name='Doc_Type' class='form-control'>  <option  value='' selected>تمام مدارک</option>
  <option  value='a'>متون چاپی</option>
  <option  value='m'>برنامه&zwnj;ها و فایلهای کامپیوتری</option>
</select><input type='text' name='user_query' class='form-control' data-toggle='tooltip' title='' name='copyNo' placeholder='عبارت مورد جستجو' value='' >	<div class='input-group-append'>			
								<button type='submit' name='ok' class='btn btn-primary' data-toggle='tooltip' title='جستجو'><svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-search' viewBox='0 0 16 16'><path d='M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z'/></svg></button>				
							</div>
            </div>
		</form>
                                            
    <script type='text/javascript'>document.search_input.user_query.focus();</script>

				</div>
			</div>
			
		</nav>
	</div>
  
	<div class='container-fluid' id='container' style='min-height: 60%;'><div class='row'>
	
		<div class='col-sm-8'>
	
	
<div id='aut_details'>

		<h3><span>رده‌بندی های مشابه :</span></h3>

		<div id='aut_details_container'>
<div id='aut_see'>
<h3>QA155</h3>
<br /><div style='margin-left:48px'><a href=./index.php?lvl=class_nbr_see&id=3218&cls_plan=1&main= ><img src='./images/folder.gif' border='0'> QA135 </a><br /><a href=./index.php?lvl=class_nbr_see&id=826&cls_plan=1&main= ><img src='./images/folder.gif' border='0'> QA135/5 </a><br /><a href=./index.php?lvl=class_nbr_see&id=2676&cls_plan=1&main= ><img src='./images/folder.gif' border='0'> QA135/6 </a><br /><a href=./index.php?lvl=class_nbr_see&id=3134&cls_plan=1&main= ><img src='./images/folder.gif' border='0'> QA155/7 </a><br /></div>	</div><!-- closing #aut_see -->

		<div id="aut_details_list_">
<h3><span>رکوردهای موجود با شماره رده : QA155</span></h3><a href='javascript:expandAll_ajax(2)'><img class='img_plusplus' src='./images/expand_all.gif' border='0' id='expandall'></a>&nbsp;<a href='javascript:collaps_all()'><img class='img_moinsmoins' src='./images/collapse_all.gif' border='0' id='collaps_all'></a>&nbsp;<a class='badge badge-info' href='index.php?lvl=sort&page_in_progress=cls_plan%3D1%26id%3D2088%26lvl%3Dclass_nbr_see' alt="مرتب سازی" title="مرتب سازی"><span class='bi bi-sort-alpha-down'></span>&nbsp;مرتب سازی</a>&nbsp;&nbsp;&nbsp;&nbsp;<a class='badge badge-info' href=#  onClick="w=window.open('./do_reserve.php?lvl=make_sugg&Dorsrv=popup','dDorsrv','scrollbars=yes,width=600,height=600,menubar=0,resizable=yes'); w.focus(); return false;" ><span class='bi bi-minecart-loaded'></span>&nbsp;درج پیشنهاد خرید</a>&nbsp;&nbsp;<a class='badge badge-info' href='./index.php?srch_type=extd_srch&disp_mode=displ_s_srch'><span class='bi bi-funnel-fill'></span>&nbsp;پالایش جستجو</a><blockquote class='no_brd'>
<div id="el8810Parent" class="parent-record">
                            <img class='img_plus' src="../opac/images/plus.gif" name="imEx" id="el8810Img" title="جزئیات" border="0" onClick="expandBase('el8810', true); return false;" hspace="3"/>
				<a href='#' onClick='show_frame("record_view.php?id=8810")'><img src='./images/search.gif' align='top' name='imEx'  border='0' /></a><img src="../opac/images/doc_type/icon_m_16x16.gif" alt=''تک نگاشت': برنامه‌ها و فایلهای کامپیوتری' title=''تک نگاشت': برنامه‌ها و فایلهای کامپیوتری'/>		
				<span class="record-header" draggable="yes" dragtype="record" id="drag_REC_8810"><span  record='8810'  class='header_title'>Instructor's solution manual single variable (2014)</span> / <a href='./index.php?lvl=author_see&id=10380' >Thomas ، George Brinton (1914)</a>، نویسنده</span>
                                <br />
				</div>				
				<div id="el8810Child" class="jumbotron arrow" style="display:none;padding-top: 10px;" >					
                                <table width='100%'><tr><td valign='top'><ul id='tabs_isbd_public'>
			<a href='index.php?lvl=record_display&id=8810' class='bi bi-zoom-in' data-toggle='tooltip' title='نمایش با جزئیات بیشتر'></a>
					
				</ul>
				<div class='row'></div>
		    	<div id='div_public8810' style='display:block;'><table><tr><td align='right' class='bg-grey'><span class='Fld_label'>نوع مدرک:</span></td><td>برنامه‌ها و فایلهای کامپیوتری</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>سرشناسه</span></td><td><a href='./index.php?lvl=author_see&id=10380' >Thomas ، George Brinton (1914)</a>، نویسنده</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>شماره بازیابی :</span></td><td><a href='./index.php?lvl=class_nbr_see&id=2088&cls_plan=1' >QA155</a>  .2014</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>عنوان :</span></td><td><span class='public_title'>Instructor's solution manual single variable&nbsp;: Thomas's calculus early transcendentals</span></td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>تکرار نام مولف :</span></td><td>George B. Thomas, Jr revised by Maurice D. Weir, Joel Hass with the assistance of Christopher Heil</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>ناشر:</span></td><td><a href='./index.php?lvl=publisher_see&id=2116' >Boston [United State of Amarica] : Pearson</a></td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>سال نشر :</span></td><td>2014</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>شابک/شاپا</span></td><td>978-0-321-88408-4</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>شناسه افزوده :</span></td><td><a href='./index.php?lvl=author_see&id=10671' >Weir ، Maurice D</a> </br> <a href='./index.php?lvl=author_see&id=10672' >Hass ، Joel</a> </br> <a href='./index.php?lvl=author_see&id=10673' >Heil ، Christopher</a></td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>لینک ثابت رکورد:</span></td><td><a href='../opac/index.php?lvl=record_display&id=8810'>../opac/index.php?lvl=record_display&id=8810</a></td></tr><span class='Z3988' title='ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=Instructor%27s%20solution%20manual%20single%20variable&amp;rft.title=Instructor%27s%20solution%20manual%20single%20variable&amp;rft.isbn=978-0-321-88408-4&amp;rft.date=2014&rft_id=..%2Fopac%2Findex.php%3Flvl%3Drecord_display%26id%3D8810&amp;rft.pub=Pearson&amp;rft.place=Boston&amp;rft.aulast=Thomas&amp;rft.aufirst=George%20Brinton&amp;rft.aulast=Weir&amp;rft.aufirst=Maurice%20D&amp;rft.aulast=Hass&amp;rft.aufirst=Joel&amp;rft.aulast=Heil&amp;rft.aufirst=Christopher'></span><tr><td align='right' class='bg-grey'><span class='Fld_label'>زبان مدرک :</span></td><td>English <span class='Fld_label'>زبان اصلی :</span> English</td></tr></table>
</div>
				<div id='div_isbd8810' style='display:none;'></div></td><td valign='middle' align='left'><img class='thumbnail thumbnail_img' src='../opac/images/no_img.png' align='right' hspace='4' vspace='2' isbn='978-0-321-88408-4' url_image='../opac/disp_rocord_img.php?url_image=http%3A%2F%2Flocalhost%2Fdoc_pic%2F%21%21isbn%21%21.jpg&recordCode=!!recordCode!!&thumbnail_url=' thumbnail_url="" /></td></tr></table>
					<br/><a class='btn btn-primary' href='#' onClick="if(confirm('آیا مایل به رزرو این مدرک هستید؟')){w=window.open('./do_reserve.php?lvl=rsrv&id_record=8810&id_Perd_Iss=0&Dorsrv=popup','dDorsrv','scrollbars=yes,width=500,height=600,menubar=0,resizable=yes'); w.focus(); return false;}else return false;" id="bt_reserve"><span class='bi bi-flag'></span>&nbsp;درخواست رزرو</a><br/><br /><div class='card border-primary' style='margin-top: 10px;'>
			<div class='card-header bg-primary'>
				<h4>
					<a class='uncollapse text-white' data-toggle='collapse' href='#hld_nb_8810'>&nbsp;فهرست موجودی مدرک</a>
				</h4>
			</div>            
			<div id='hld_nb_8810' class=''>
				<table class='table table-striped table-hover'><thead><th class='copy_header_hld_nbr'>شماره ثبت</th><th class='copy_header_copy_call_num'>شماره بازیابی</th><th class='copy_header_doc_typ_name'>نام عام مواد</th><th class='copy_header_loc_name'>محل نگهداری</th><th class='copy_header_section_label'>بخش</th><th class='copy_header_status_label'>وضعیت ثبت</th><th>وضعیت امانت</th></thead><tr><td class='hld_nbr'>0118000032</td><td class='copy_call_num'>QA155 .2014 </td><td class='doc_typ_name'>منابع الکترونیکی:کتاب</td><td class='loc_name'>دانشگاه خاتم النبیین(ص)-کابل</td><td class='section_label'>سایر</td><td class='status_label'>اسناد معمولی</td><td class='copy_situation'><strong>موجود</strong> </td></tr>	
	</table>
			</div>
		</div><div class='card border-primary' style='margin-top: 10px;'>
			<div class='card-header bg-primary'>
				<h4>
					<a class='uncollapse text-white' data-toggle='collapse' href='#opn_8810'>&nbsp;نظرهای کاربران درباره این مدرک</a>
				</h4>
			</div>            
			<div id='opn_8810' class='card-body collapse show'>
				<h4><a href='#' onclick="show_add_opinion(8810); return false;">تعداد نظرات کاربران :0 . برای افزودن نظر خود کلیک نمایید.</a></h4>
					
	
	<script type='text/javascript' src='./includes/javascript/bbcode.js'></script>		
	<script type='text/javascript'>
	<!--	
		function show_add_opinion(record_id) {
			var div_add_opinion=document.getElementById('add_opinion_'+record_id);
			if(div_add_opinion.style.display  == 'block'){
				div_add_opinion.style.display  = 'none';
			}else{
				div_add_opinion.style.display  = 'block';
			}				
		}
		
		function send_opinion(record_id) {		
			var note=3;
		 	var btns_note = document.getElementsByName('opinion_note_'+record_id);
			
		 	if(btns_note.length == 1) {
			
		 		btns_note = document.getElementById('opinion_note_'+record_id);
		 		if(btns_note){
				 	var selIndex = btns_note.selectedIndex;				
					note = btns_note.options[selIndex].value;	
				}		 		
		 	} else {
				for (var i=0; i < btns_note.length; i++) {
	                if (btns_note[i].checked) {
	                    note=i + 1;
	                }
	            }
	        }    					
			var subject=document.getElementById('edit_subject_'+record_id).value;	
			var CMNT=document.getElementById('edit_comment_'+record_id).value;	
			if(	subject  || CMNT){		
				var url= './ajax.php?module=ajax&categ=opinion&sub=add&id_borrower=';
				url+='&note='+note;
				url+='&record_id='+record_id;
				
				// class initialization:
				var req = new http_request();
				// query execution
				req.request(url, true, 'subject='+encodeURIComponent(subject)+'&CMNT='+encodeURIComponent(CMNT));
				
				document.getElementById('add_opinion_'+record_id).innerHTML = '<label class="alert alert-info">نظر شما راجع به این رکورد ثبت شد و بعد از تایید کتابدار قابل رویت خواهد بود.</label>';
			}	
			return 1;
		}			
	-->
	</script>

	<div id='add_opinion_8810' style='display: none;'>
				
		<div class='row'><label>رای شما :</label>
			<select class='form-control col-md-12' id='opinion_note_8810' name='opinion_note_8810'>
				<option value='0'>بدون امتیاز</option>
				<option value='1'>بد</option>
				<option value='2'>ضعیف</option>
				<option value='3' selected='selected'>خوب</option>
				<option value='4'>بسیار خوب</option>
				<option value='5'>جذاب</option>
			</select>
		</div>
	
		<div class='row'><label>موضوع</label><br />
			<input class='form-control col-md-12' type='text' name='subject' id='edit_subject_8810' size='50'/>
		</div>
		<div class='row'>
			<span class='right'><label>شرح نظر شما</label></span>			
			<span class='left'>
				<input value=' B ' name='B' onclick="insert_text('edit_comment_8810','[b]','[/b]')" type='button' class='btn'> 
				<input value=' I ' name='I' onclick="insert_text('edit_comment_8810','[i]','[/i]')" type='button' class='btn'>
				<input value=' U ' name='U' onclick="insert_text('edit_comment_8810','[u]','[/u]')" type='button' class='btn'>
				<input value='http://' name='Url' onclick="insert_text('edit_comment_8810','[url]','[/url]')" type='button' class='btn'>
				<input value='Img' name='Img' onclick="insert_text('edit_comment_8810','[img]','[/img]')" type='button' class='btn'>
				<input value='Code' name='Code' onclick="insert_text('edit_comment_8810','[code]','[/code]')" type='button' class='btn'>
				<input value='Quote' name='Quote' onclick="insert_text('edit_comment_8810','[quote]','[/quote]')" type='button' class='btn'>
			</span>
		</div>		
		<div class='row'>
			<textarea class='form-control col-md-12' name='CMNT' id='edit_comment_8810' cols='60' rows='2'></textarea>
		</div>
      	<div class='row'>
	        <input type='button' class='btn' onclick=" send_opinion(8810);  return false; " value='ارسال'>
		</div>
	</div>

			</div>
		</div></div><div id="el14513Parent" class="parent-record">
                            <img class='img_plus' src="../opac/images/plus.gif" name="imEx" id="el14513Img" title="جزئیات" border="0" onClick="expandBase('el14513', true); return false;" hspace="3"/>
				<a href='#' onClick='show_frame("record_view.php?id=14513")'><img src='./images/search.gif' align='top' name='imEx'  border='0' /></a><img src="../opac/images/doc_type/icon_a.png" alt=''تک نگاشت': متون چاپی' title=''تک نگاشت': متون چاپی'/>		
				<span class="record-header" draggable="yes" dragtype="record" id="drag_REC_14513"><span  record='14513'  class='header_title'>الجبر خطی (1396)</span> / <a href='./index.php?lvl=author_see&id=13493' >غوری ، محمد انور</a>، نویسنده</span>
                                <br />
				</div>				
				<div id="el14513Child" class="jumbotron arrow" style="display:none;padding-top: 10px;" >					
                                <table width='100%'><tr><td><ul id='tabs_isbd_public'>
			<a href='index.php?lvl=record_display&id=14513' class='bi bi-zoom-in' data-toggle='tooltip' title='نمایش با جزئیات بیشتر'></a>
					
				</ul>
				<div class='row'></div>
		    	<div id='div_public14513' style='display:block;'><table><tr><td align='right' class='bg-grey'><span class='Fld_label'>نوع مدرک:</span></td><td>متون چاپی</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>سرشناسه</span></td><td><a href='./index.php?lvl=author_see&id=13493' >غوری ، محمد انور</a>، نویسنده</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>شماره بازیابی :</span></td><td><a href='./index.php?lvl=class_nbr_see&id=2088&cls_plan=1' >QA155</a>  ‭/1396</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>عنوان :</span></td><td><span class='public_title'>الجبر خطی</span></td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>تکرار نام مولف :</span></td><td>مولفان: پوهاند دکتر محمد انور غوری و پوهندوی محمد خان حیدری</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>ناشر:</span></td><td><a href='./index.php?lvl=publisher_see&id=371' >کابل : سعید</a></td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>سال نشر :</span></td><td>1396</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>شناسه افزوده :</span></td><td><a href='./index.php?lvl=author_see&id=13494' >حیدری ، محمد خان</a></td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>موضوع‌ها :</span></td><td><b>اصفا</b><br /><a href='./index.php?lvl=SubjHead_see&id=8742' >جبر خطی</a><br /></td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>لینک ثابت رکورد:</span></td><td><a href='../opac/index.php?lvl=record_display&id=14513'>../opac/index.php?lvl=record_display&id=14513</a></td></tr><span class='Z3988' title='ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=%C3%98%C2%A7%C3%99%C2%84%C3%98%C2%AC%C3%98%C2%A8%C3%98%C2%B1%20%C3%98%C2%AE%C3%98%C2%B7%C3%9B%C2%8C&amp;rft.title=%C3%98%C2%A7%C3%99%C2%84%C3%98%C2%AC%C3%98%C2%A8%C3%98%C2%B1%20%C3%98%C2%AE%C3%98%C2%B7%C3%9B%C2%8C&amp;rft.date=1396&rft_id=..%2Fopac%2Findex.php%3Flvl%3Drecord_display%26id%3D14513&amp;rft.pub=%C3%98%C2%B3%C3%98%C2%B9%C3%9B%C2%8C%C3%98%C2%AF&amp;rft.place=%C3%9A%C2%A9%C3%98%C2%A7%C3%98%C2%A8%C3%99%C2%84&amp;rft.aulast=%C3%98%C2%BA%C3%99%C2%88%C3%98%C2%B1%C3%9B%C2%8C&amp;rft.aufirst=%C3%99%C2%85%C3%98%C2%AD%C3%99%C2%85%C3%98%C2%AF%20%C3%98%C2%A7%C3%99%C2%86%C3%99%C2%88%C3%98%C2%B1&amp;rft.aulast=%C3%98%C2%AD%C3%9B%C2%8C%C3%98%C2%AF%C3%98%C2%B1%C3%9B%C2%8C&amp;rft.aufirst=%C3%99%C2%85%C3%98%C2%AD%C3%99%C2%85%C3%98%C2%AF%20%C3%98%C2%AE%C3%98%C2%A7%C3%99%C2%86'></span><tr><td align='right' class='bg-grey'><span class='Fld_label'>زبان مدرک :</span></td><td>فارسی</td></tr></table>
</div>
				<div id='div_isbd14513' style='display:none;'></div></td></tr></table>
					<br/><a class='btn btn-primary' href='#' onClick="if(confirm('آیا مایل به رزرو این مدرک هستید؟')){w=window.open('./do_reserve.php?lvl=rsrv&id_record=14513&id_Perd_Iss=0&Dorsrv=popup','dDorsrv','scrollbars=yes,width=500,height=600,menubar=0,resizable=yes'); w.focus(); return false;}else return false;" id="bt_reserve"><span class='bi bi-flag'></span>&nbsp;درخواست رزرو</a><br/><br /><div class='card border-primary' style='margin-top: 10px;'>
			<div class='card-header bg-primary'>
				<h4>
					<a class='uncollapse text-white' data-toggle='collapse' href='#hld_nb_14513'>&nbsp;فهرست موجودی مدرک</a>
				</h4>
			</div>            
			<div id='hld_nb_14513' class=''>
				<table class='table table-striped table-hover'><thead><th class='copy_header_hld_nbr'>شماره ثبت</th><th class='copy_header_copy_call_num'>شماره بازیابی</th><th class='copy_header_doc_typ_name'>نام عام مواد</th><th class='copy_header_loc_name'>محل نگهداری</th><th class='copy_header_section_label'>بخش</th><th class='copy_header_status_label'>وضعیت ثبت</th><th>وضعیت امانت</th></thead><tr><td class='hld_nbr'>25655</td><td class='copy_call_num'>QA155 ‭/1396 </td><td class='doc_typ_name'>کتاب فارسی</td><td class='loc_name'>دانشگاه خاتم النبیین(ص)-کابل</td><td class='section_label'>علمی و آموزشی</td><td class='status_label'>اسناد معمولی</td><td class='copy_situation'><strong>تاریخ بازگشت ۱۴۰۴/۰۷/۲۴</strong> </td></tr><tr><td class='hld_nbr'>25848</td><td class='copy_call_num'>QA155 ‭/1396 ن.2</td><td class='doc_typ_name'>کتاب فارسی</td><td class='loc_name'>دانشگاه خاتم النبیین(ص)-کابل</td><td class='section_label'>علمی و آموزشی</td><td class='status_label'>اسناد معمولی</td><td class='copy_situation'><strong>موجود</strong> </td></tr><tr><td class='hld_nbr'>25849</td><td class='copy_call_num'>QA155 ‭/1396 ن.3</td><td class='doc_typ_name'>کتاب فارسی</td><td class='loc_name'>دانشگاه خاتم النبیین(ص)-کابل</td><td class='section_label'>علمی و آموزشی</td><td class='status_label'>اسناد معمولی</td><td class='copy_situation'><strong>موجود</strong> </td></tr><tr><td class='hld_nbr'>25850</td><td class='copy_call_num'>QA155 ‭/1396 ن.4</td><td class='doc_typ_name'>کتاب فارسی</td><td class='loc_name'>دانشگاه خاتم النبیین(ص)-کابل</td><td class='section_label'>علمی و آموزشی</td><td class='status_label'>اسناد معمولی</td><td class='copy_situation'><strong>موجود</strong> </td></tr><tr><td class='hld_nbr'>25851</td><td class='copy_call_num'>QA155 ‭/1396 ن.5</td><td class='doc_typ_name'>کتاب فارسی</td><td class='loc_name'>دانشگاه خاتم النبیین(ص)-کابل</td><td class='section_label'>علمی و آموزشی</td><td class='status_label'>اسناد معمولی</td><td class='copy_situation'><strong>تاریخ بازگشت ۱۴۰۵/۰۲/۲۶</strong> </td></tr><tr><td class='hld_nbr'>25852</td><td class='copy_call_num'>QA155 ‭/1396 ن.6</td><td class='doc_typ_name'>کتاب فارسی</td><td class='loc_name'>دانشگاه خاتم النبیین(ص)-کابل</td><td class='section_label'>علمی و آموزشی</td><td class='status_label'>اسناد معمولی</td><td class='copy_situation'><strong>تاریخ بازگشت ۱۴۰۴/۰۸/۰۶</strong> </td></tr>	
	</table>
			</div>
		</div><div class='card border-primary' style='margin-top: 10px;'>
			<div class='card-header bg-primary'>
				<h4>
					<a class='uncollapse text-white' data-toggle='collapse' href='#opn_14513'>&nbsp;نظرهای کاربران درباره این مدرک</a>
				</h4>
			</div>            
			<div id='opn_14513' class='card-body collapse show'>
				<h4><a href='#' onclick="show_add_opinion(14513); return false;">تعداد نظرات کاربران :0 . برای افزودن نظر خود کلیک نمایید.</a></h4>
					
	
	<script type='text/javascript' src='./includes/javascript/bbcode.js'></script>		
	<script type='text/javascript'>
	<!--	
		function show_add_opinion(record_id) {
			var div_add_opinion=document.getElementById('add_opinion_'+record_id);
			if(div_add_opinion.style.display  == 'block'){
				div_add_opinion.style.display  = 'none';
			}else{
				div_add_opinion.style.display  = 'block';
			}				
		}
		
		function send_opinion(record_id) {		
			var note=3;
		 	var btns_note = document.getElementsByName('opinion_note_'+record_id);
			
		 	if(btns_note.length == 1) {
			
		 		btns_note = document.getElementById('opinion_note_'+record_id);
		 		if(btns_note){
				 	var selIndex = btns_note.selectedIndex;				
					note = btns_note.options[selIndex].value;	
				}		 		
		 	} else {
				for (var i=0; i < btns_note.length; i++) {
	                if (btns_note[i].checked) {
	                    note=i + 1;
	                }
	            }
	        }    					
			var subject=document.getElementById('edit_subject_'+record_id).value;	
			var CMNT=document.getElementById('edit_comment_'+record_id).value;	
			if(	subject  || CMNT){		
				var url= './ajax.php?module=ajax&categ=opinion&sub=add&id_borrower=';
				url+='&note='+note;
				url+='&record_id='+record_id;
				
				// class initialization:
				var req = new http_request();
				// query execution
				req.request(url, true, 'subject='+encodeURIComponent(subject)+'&CMNT='+encodeURIComponent(CMNT));
				
				document.getElementById('add_opinion_'+record_id).innerHTML = '<label class="alert alert-info">نظر شما راجع به این رکورد ثبت شد و بعد از تایید کتابدار قابل رویت خواهد بود.</label>';
			}	
			return 1;
		}			
	-->
	</script>

	<div id='add_opinion_14513' style='display: none;'>
				
		<div class='row'><label>رای شما :</label>
			<select class='form-control col-md-12' id='opinion_note_14513' name='opinion_note_14513'>
				<option value='0'>بدون امتیاز</option>
				<option value='1'>بد</option>
				<option value='2'>ضعیف</option>
				<option value='3' selected='selected'>خوب</option>
				<option value='4'>بسیار خوب</option>
				<option value='5'>جذاب</option>
			</select>
		</div>
	
		<div class='row'><label>موضوع</label><br />
			<input class='form-control col-md-12' type='text' name='subject' id='edit_subject_14513' size='50'/>
		</div>
		<div class='row'>
			<span class='right'><label>شرح نظر شما</label></span>			
			<span class='left'>
				<input value=' B ' name='B' onclick="insert_text('edit_comment_14513','[b]','[/b]')" type='button' class='btn'> 
				<input value=' I ' name='I' onclick="insert_text('edit_comment_14513','[i]','[/i]')" type='button' class='btn'>
				<input value=' U ' name='U' onclick="insert_text('edit_comment_14513','[u]','[/u]')" type='button' class='btn'>
				<input value='http://' name='Url' onclick="insert_text('edit_comment_14513','[url]','[/url]')" type='button' class='btn'>
				<input value='Img' name='Img' onclick="insert_text('edit_comment_14513','[img]','[/img]')" type='button' class='btn'>
				<input value='Code' name='Code' onclick="insert_text('edit_comment_14513','[code]','[/code]')" type='button' class='btn'>
				<input value='Quote' name='Quote' onclick="insert_text('edit_comment_14513','[quote]','[/quote]')" type='button' class='btn'>
			</span>
		</div>		
		<div class='row'>
			<textarea class='form-control col-md-12' name='CMNT' id='edit_comment_14513' cols='60' rows='2'></textarea>
		</div>
      	<div class='row'>
	        <input type='button' class='btn' onclick=" send_opinion(14513);  return false; " value='ارسال'>
		</div>
	</div>

			</div>
		</div></div><div id="el8809Parent" class="parent-record">
                            <img class='img_plus' src="../opac/images/plus.gif" name="imEx" id="el8809Img" title="جزئیات" border="0" onClick="expandBase('el8809', true); return false;" hspace="3"/>
				<a href='#' onClick='show_frame("record_view.php?id=8809")'><img src='./images/search.gif' align='top' name='imEx'  border='0' /></a><img src="../opac/images/doc_type/icon_m_16x16.gif" alt=''تک نگاشت': برنامه‌ها و فایلهای کامپیوتری' title=''تک نگاشت': برنامه‌ها و فایلهای کامپیوتری'/>		
				<span class="record-header" draggable="yes" dragtype="record" id="drag_REC_8809"><span  record='8809'  class='header_title'>جبر خطی</span> / <a href='./index.php?lvl=author_see&id=10668' >هافمن ، کنت</a>، نویسنده</span>&nbsp;<span><a href="./digi_doc.php?digcopy_id=42" target="__LINK__"><img src="./images/attachment.png" border="0" align="middle" hspace="3" alt="بازکردن سند8809.PDF" title="بازکردن سند8809.PDF"></a></span>
                                <br />
				</div>				
				<div id="el8809Child" class="jumbotron arrow" style="display:none;padding-top: 10px;" >					
                                <table width='100%'><tr><td><ul id='tabs_isbd_public'>
			<a href='index.php?lvl=record_display&id=8809' class='bi bi-zoom-in' data-toggle='tooltip' title='نمایش با جزئیات بیشتر'></a>
					
				</ul>
				<div class='row'></div>
		    	<div id='div_public8809' style='display:block;'><table><tr><td align='right' class='bg-grey'><span class='Fld_label'>نوع مدرک:</span></td><td>برنامه‌ها و فایلهای کامپیوتری</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>سرشناسه</span></td><td><a href='./index.php?lvl=author_see&id=10668' >هافمن ، کنت</a>، نویسنده</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>شماره بازیابی :</span></td><td><a href='./index.php?lvl=class_nbr_see&id=2088&cls_plan=1' >QA155</a>  ‭/</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>عنوان :</span></td><td><span class='public_title'>جبر خطی</span></td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>تکرار نام مولف :</span></td><td>کنت هافمن، ری کنزی ترجمه جمشید فرشیدی</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>ناشر:</span></td><td><a href='./index.php?lvl=publisher_see&id=18' >تهران : مرکز نشر دانشگاهی</a></td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>شناسه افزوده :</span></td><td><a href='./index.php?lvl=author_see&id=10669' >کنزی ، ری</a> </br> <a href='./index.php?lvl=author_see&id=10670' >فرشیدی ، جمشید</a>، مترجم</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>لینک ثابت رکورد:</span></td><td><a href='../opac/index.php?lvl=record_display&id=8809'>../opac/index.php?lvl=record_display&id=8809</a></td></tr><span class='Z3988' title='ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=%C3%98%C2%AC%C3%98%C2%A8%C3%98%C2%B1%20%C3%98%C2%AE%C3%98%C2%B7%C3%9B%C2%8C&amp;rft.title=%C3%98%C2%AC%C3%98%C2%A8%C3%98%C2%B1%20%C3%98%C2%AE%C3%98%C2%B7%C3%9B%C2%8C&rft_id=..%2Fopac%2Findex.php%3Flvl%3Drecord_display%26id%3D8809&amp;rft.pub=%C3%99%C2%85%C3%98%C2%B1%C3%9A%C2%A9%C3%98%C2%B2%20%C3%99%C2%86%C3%98%C2%B4%C3%98%C2%B1%20%C3%98%C2%AF%C3%98%C2%A7%C3%99%C2%86%C3%98%C2%B4%C3%9A%C2%AF%C3%98%C2%A7%C3%99%C2%87%C3%9B%C2%8C&amp;rft.place=%C3%98%C2%AA%C3%99%C2%87%C3%98%C2%B1%C3%98%C2%A7%C3%99%C2%86&amp;rft.aulast=%C3%99%C2%87%C3%98%C2%A7%C3%99%C2%81%C3%99%C2%85%C3%99%C2%86&amp;rft.aufirst=%C3%9A%C2%A9%C3%99%C2%86%C3%98%C2%AA&amp;rft.aulast=%C3%9A%C2%A9%C3%99%C2%86%C3%98%C2%B2%C3%9B%C2%8C&amp;rft.aufirst=%C3%98%C2%B1%C3%9B%C2%8C&amp;rft.aulast=%C3%99%C2%81%C3%98%C2%B1%C3%98%C2%B4%C3%9B%C2%8C%C3%98%C2%AF%C3%9B%C2%8C&amp;rft.aufirst=%C3%98%C2%AC%C3%99%C2%85%C3%98%C2%B4%C3%9B%C2%8C%C3%98%C2%AF'></span><tr><td align='right' class='bg-grey'><span class='Fld_label'>زبان مدرک :</span></td><td>فارسی <span class='Fld_label'>زبان اصلی :</span> English</td></tr></table>
</div>
				<div id='div_isbd8809' style='display:none;'></div></td></tr></table>
					<br/><a class='btn btn-primary' href='#' onClick="if(confirm('آیا مایل به رزرو این مدرک هستید؟')){w=window.open('./do_reserve.php?lvl=rsrv&id_record=8809&id_Perd_Iss=0&Dorsrv=popup','dDorsrv','scrollbars=yes,width=500,height=600,menubar=0,resizable=yes'); w.focus(); return false;}else return false;" id="bt_reserve"><span class='bi bi-flag'></span>&nbsp;درخواست رزرو</a><br/><br /><div class='card border-primary' style='margin-top: 10px;'>
			<div class='card-header bg-primary'>
				<h4>
					<a class='uncollapse text-white' data-toggle='collapse' href='#hld_nb_8809'>&nbsp;فهرست موجودی مدرک</a>
				</h4>
			</div>            
			<div id='hld_nb_8809' class=''>
				<table class='table table-striped table-hover'><thead><th class='copy_header_hld_nbr'>شماره ثبت</th><th class='copy_header_copy_call_num'>شماره بازیابی</th><th class='copy_header_doc_typ_name'>نام عام مواد</th><th class='copy_header_loc_name'>محل نگهداری</th><th class='copy_header_section_label'>بخش</th><th class='copy_header_status_label'>وضعیت ثبت</th><th>وضعیت امانت</th></thead><tr><td class='hld_nbr'>0118000031</td><td class='copy_call_num'>QA155 ‭/ </td><td class='doc_typ_name'>منابع الکترونیکی:کتاب</td><td class='loc_name'>دانشگاه خاتم النبیین(ص)-کابل</td><td class='section_label'>کامپیوتر ساینس</td><td class='status_label'>اسناد معمولی</td><td class='copy_situation'><strong>موجود</strong> </td></tr>	
	</table>
			</div>
		</div><div class='panel panel-primary' style='margin-top: 10px;'>
			<div class='card-header bg-primary'>
				<h4>
					<a class='uncollapse text-white' data-toggle='collapse' href='#8809'>&nbsp;نسخه‌های الکترونیک مرتبط با رکورد</a>
				</h4>
			</div>            
			<div id='8809' class='card-body collapse show'>
				<table class='table-no-border'><tr>
								<td class='digi-cell'><div class='panel panel-default'><a href='../opac/digi_doc.php?digcopy_id=42' alt='8809.PDF - application/pdf' title='8809.PDF - application/pdf' target='_blank'><img src='../opac/images/mimetype/pdf-dist.png' alt='8809.PDF - application/pdf' title='8809.PDF - application/pdf' border='0'></a><br /><small>Adobe Acrobat P...</small><div class='panel-footer clearfix'><small>8809.PDF</small></div></div></td>
								<td class='digi-cell'>&nbsp;</td>
								<td class='digi-cell'>&nbsp;</td>
								<td class='digi-cell'>&nbsp;</td>
								<td class='digi-cell'>&nbsp;</td>
							</tr></table>
			</div>
		</div><div class='card border-primary' style='margin-top: 10px;'>
			<div class='card-header bg-primary'>
				<h4>
					<a class='uncollapse text-white' data-toggle='collapse' href='#opn_8809'>&nbsp;نظرهای کاربران درباره این مدرک</a>
				</h4>
			</div>            
			<div id='opn_8809' class='card-body collapse show'>
				<h4><a href='#' onclick="show_add_opinion(8809); return false;">تعداد نظرات کاربران :0 . برای افزودن نظر خود کلیک نمایید.</a></h4>
					
	
	<script type='text/javascript' src='./includes/javascript/bbcode.js'></script>		
	<script type='text/javascript'>
	<!--	
		function show_add_opinion(record_id) {
			var div_add_opinion=document.getElementById('add_opinion_'+record_id);
			if(div_add_opinion.style.display  == 'block'){
				div_add_opinion.style.display  = 'none';
			}else{
				div_add_opinion.style.display  = 'block';
			}				
		}
		
		function send_opinion(record_id) {		
			var note=3;
		 	var btns_note = document.getElementsByName('opinion_note_'+record_id);
			
		 	if(btns_note.length == 1) {
			
		 		btns_note = document.getElementById('opinion_note_'+record_id);
		 		if(btns_note){
				 	var selIndex = btns_note.selectedIndex;				
					note = btns_note.options[selIndex].value;	
				}		 		
		 	} else {
				for (var i=0; i < btns_note.length; i++) {
	                if (btns_note[i].checked) {
	                    note=i + 1;
	                }
	            }
	        }    					
			var subject=document.getElementById('edit_subject_'+record_id).value;	
			var CMNT=document.getElementById('edit_comment_'+record_id).value;	
			if(	subject  || CMNT){		
				var url= './ajax.php?module=ajax&categ=opinion&sub=add&id_borrower=';
				url+='&note='+note;
				url+='&record_id='+record_id;
				
				// class initialization:
				var req = new http_request();
				// query execution
				req.request(url, true, 'subject='+encodeURIComponent(subject)+'&CMNT='+encodeURIComponent(CMNT));
				
				document.getElementById('add_opinion_'+record_id).innerHTML = '<label class="alert alert-info">نظر شما راجع به این رکورد ثبت شد و بعد از تایید کتابدار قابل رویت خواهد بود.</label>';
			}	
			return 1;
		}			
	-->
	</script>

	<div id='add_opinion_8809' style='display: none;'>
				
		<div class='row'><label>رای شما :</label>
			<select class='form-control col-md-12' id='opinion_note_8809' name='opinion_note_8809'>
				<option value='0'>بدون امتیاز</option>
				<option value='1'>بد</option>
				<option value='2'>ضعیف</option>
				<option value='3' selected='selected'>خوب</option>
				<option value='4'>بسیار خوب</option>
				<option value='5'>جذاب</option>
			</select>
		</div>
	
		<div class='row'><label>موضوع</label><br />
			<input class='form-control col-md-12' type='text' name='subject' id='edit_subject_8809' size='50'/>
		</div>
		<div class='row'>
			<span class='right'><label>شرح نظر شما</label></span>			
			<span class='left'>
				<input value=' B ' name='B' onclick="insert_text('edit_comment_8809','[b]','[/b]')" type='button' class='btn'> 
				<input value=' I ' name='I' onclick="insert_text('edit_comment_8809','[i]','[/i]')" type='button' class='btn'>
				<input value=' U ' name='U' onclick="insert_text('edit_comment_8809','[u]','[/u]')" type='button' class='btn'>
				<input value='http://' name='Url' onclick="insert_text('edit_comment_8809','[url]','[/url]')" type='button' class='btn'>
				<input value='Img' name='Img' onclick="insert_text('edit_comment_8809','[img]','[/img]')" type='button' class='btn'>
				<input value='Code' name='Code' onclick="insert_text('edit_comment_8809','[code]','[/code]')" type='button' class='btn'>
				<input value='Quote' name='Quote' onclick="insert_text('edit_comment_8809','[quote]','[/quote]')" type='button' class='btn'>
			</span>
		</div>		
		<div class='row'>
			<textarea class='form-control col-md-12' name='CMNT' id='edit_comment_8809' cols='60' rows='2'></textarea>
		</div>
      	<div class='row'>
	        <input type='button' class='btn' onclick=" send_opinion(8809);  return false; " value='ارسال'>
		</div>
	</div>

			</div>
		</div></div><div id="el3979Parent" class="parent-record">
                            <img class='img_plus' src="../opac/images/plus.gif" name="imEx" id="el3979Img" title="جزئیات" border="0" onClick="expandBase('el3979', true); return false;" hspace="3"/>
				<a href='#' onClick='show_frame("record_view.php?id=3979")'><img src='./images/search.gif' align='top' name='imEx'  border='0' /></a><img src="../opac/images/doc_type/icon_a.png" alt=''تک نگاشت': متون چاپی' title=''تک نگاشت': متون چاپی'/>		
				<span class="record-header" draggable="yes" dragtype="record" id="drag_REC_3979"><span  record='3979'  class='header_title'>الجبرمقدماتی (1387)</span> / <a href='./index.php?lvl=author_see&id=5062' >نورزاد ، عبدالسمیع</a>، نویسنده</span>
                                <br />
				</div>				
				<div id="el3979Child" class="jumbotron arrow" style="display:none;padding-top: 10px;" >					
                                <table width='100%'><tr><td><ul id='tabs_isbd_public'>
			<a href='index.php?lvl=record_display&id=3979' class='bi bi-zoom-in' data-toggle='tooltip' title='نمایش با جزئیات بیشتر'></a>
					
				</ul>
				<div class='row'></div>
		    	<div id='div_public3979' style='display:block;'><table><tr><td align='right' class='bg-grey'><span class='Fld_label'>نوع مدرک:</span></td><td>متون چاپی</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>سرشناسه</span></td><td><a href='./index.php?lvl=author_see&id=5062' >نورزاد ، عبدالسمیع</a>، نویسنده</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>شماره بازیابی :</span></td><td><a href='./index.php?lvl=class_nbr_see&id=2088&cls_plan=1' >QA155</a>  ‭/ط9م7 1387</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>عنوان :</span></td><td><span class='public_title'>الجبرمقدماتی</span></td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>تکرار نام مولف :</span></td><td>عبدالسمیع</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>ناشر:</span></td><td><a href='./index.php?lvl=publisher_see&id=371' >کابل : سعید</a></td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>سال نشر :</span></td><td>1387</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>صفحه شمار:</span></td><td>76ص</td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>موضوع‌ها :</span></td><td><b>اصفا</b><br /><a href='./index.php?lvl=SubjHead_see&id=5158' >جبر</a> ؛ <a href='./index.php?lvl=SubjHead_see&id=5159' >جبر -- مسائل، تمرینها و غیره</a> ؛ <a href='./index.php?lvl=SubjHead_see&id=5160' >هندسه تحلیلی</a> ؛ <a href='./index.php?lvl=SubjHead_see&id=1938' >هندسه -- مسائل، تمرینها و غیره</a><br /></td></tr><tr><td align='right' class='bg-grey'><span class='Fld_label'>لینک ثابت رکورد:</span></td><td><a href='../opac/index.php?lvl=record_display&id=3979'>../opac/index.php?lvl=record_display&id=3979</a></td></tr><span class='Z3988' title='ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=%C3%98%C2%A7%C3%99%C2%84%C3%98%C2%AC%C3%98%C2%A8%C3%98%C2%B1%C3%99%C2%85%C3%99%C2%82%C3%98%C2%AF%C3%99%C2%85%C3%98%C2%A7%C3%98%C2%AA%C3%9B%C2%8C&amp;rft.title=%C3%98%C2%A7%C3%99%C2%84%C3%98%C2%AC%C3%98%C2%A8%C3%98%C2%B1%C3%99%C2%85%C3%99%C2%82%C3%98%C2%AF%C3%99%C2%85%C3%98%C2%A7%C3%98%C2%AA%C3%9B%C2%8C&amp;rft.tpages=76%C3%98%C2%B5&amp;rft.date=1387&rft_id=..%2Fopac%2Findex.php%3Flvl%3Drecord_display%26id%3D3979&amp;rft.pub=%C3%98%C2%B3%C3%98%C2%B9%C3%9B%C2%8C%C3%98%C2%AF&amp;rft.place=%C3%9A%C2%A9%C3%98%C2%A7%C3%98%C2%A8%C3%99%C2%84&amp;rft.aulast=%C3%99%C2%86%C3%99%C2%88%C3%98%C2%B1%C3%98%C2%B2%C3%98%C2%A7%C3%98%C2%AF&amp;rft.aufirst=%C3%98%C2%B9%C3%98%C2%A8%C3%98%C2%AF%C3%98%C2%A7%C3%99%C2%84%C3%98%C2%B3%C3%99%C2%85%C3%9B%C2%8C%C3%98%C2%B9'></span><tr><td align='right' class='bg-grey'><span class='Fld_label'>زبان مدرک :</span></td><td>فارسی</td></tr></table>
</div>
				<div id='div_isbd3979' style='display:none;'></div></td></tr></table>
					<br/><a class='btn btn-primary' href='#' onClick="if(confirm('آیا مایل به رزرو این مدرک هستید؟')){w=window.open('./do_reserve.php?lvl=rsrv&id_record=3979&id_Perd_Iss=0&Dorsrv=popup','dDorsrv','scrollbars=yes,width=500,height=600,menubar=0,resizable=yes'); w.focus(); return false;}else return false;" id="bt_reserve"><span class='bi bi-flag'></span>&nbsp;درخواست رزرو</a><br/><br /><div class='card border-primary' style='margin-top: 10px;'>
			<div class='card-header bg-primary'>
				<h4>
					<a class='uncollapse text-white' data-toggle='collapse' href='#hld_nb_3979'>&nbsp;فهرست موجودی مدرک</a>
				</h4>
			</div>            
			<div id='hld_nb_3979' class=''>
				<table class='table table-striped table-hover'><thead><th class='copy_header_hld_nbr'>شماره ثبت</th><th class='copy_header_copy_call_num'>شماره بازیابی</th><th class='copy_header_doc_typ_name'>نام عام مواد</th><th class='copy_header_loc_name'>محل نگهداری</th><th class='copy_header_section_label'>بخش</th><th class='copy_header_status_label'>وضعیت ثبت</th><th>وضعیت امانت</th></thead><tr><td class='hld_nbr'>0101008936</td><td class='copy_call_num'>QA155‭ /ط9م7 1387 </td><td class='doc_typ_name'>کتاب فارسی</td><td class='loc_name'>دانشگاه خاتم النبیین(ص)-کابل</td><td class='section_label'>علمی و آموزشی</td><td class='status_label'>اسناد معمولی</td><td class='copy_situation'><strong>موجود</strong> </td></tr>	
	</table>
			</div>
		</div><div class='card border-primary' style='margin-top: 10px;'>
			<div class='card-header bg-primary'>
				<h4>
					<a class='uncollapse text-white' data-toggle='collapse' href='#opn_3979'>&nbsp;نظرهای کاربران درباره این مدرک</a>
				</h4>
			</div>            
			<div id='opn_3979' class='card-body collapse show'>
				<h4><a href='#' onclick="show_add_opinion(3979); return false;">تعداد نظرات کاربران :0 . برای افزودن نظر خود کلیک نمایید.</a></h4>
					
	
	<script type='text/javascript' src='./includes/javascript/bbcode.js'></script>		
	<script type='text/javascript'>
	<!--	
		function show_add_opinion(record_id) {
			var div_add_opinion=document.getElementById('add_opinion_'+record_id);
			if(div_add_opinion.style.display  == 'block'){
				div_add_opinion.style.display  = 'none';
			}else{
				div_add_opinion.style.display  = 'block';
			}				
		}
		
		function send_opinion(record_id) {		
			var note=3;
		 	var btns_note = document.getElementsByName('opinion_note_'+record_id);
			
		 	if(btns_note.length == 1) {
			
		 		btns_note = document.getElementById('opinion_note_'+record_id);
		 		if(btns_note){
				 	var selIndex = btns_note.selectedIndex;				
					note = btns_note.options[selIndex].value;	
				}		 		
		 	} else {
				for (var i=0; i < btns_note.length; i++) {
	                if (btns_note[i].checked) {
	                    note=i + 1;
	                }
	            }
	        }    					
			var subject=document.getElementById('edit_subject_'+record_id).value;	
			var CMNT=document.getElementById('edit_comment_'+record_id).value;	
			if(	subject  || CMNT){		
				var url= './ajax.php?module=ajax&categ=opinion&sub=add&id_borrower=';
				url+='&note='+note;
				url+='&record_id='+record_id;
				
				// class initialization:
				var req = new http_request();
				// query execution
				req.request(url, true, 'subject='+encodeURIComponent(subject)+'&CMNT='+encodeURIComponent(CMNT));
				
				document.getElementById('add_opinion_'+record_id).innerHTML = '<label class="alert alert-info">نظر شما راجع به این رکورد ثبت شد و بعد از تایید کتابدار قابل رویت خواهد بود.</label>';
			}	
			return 1;
		}			
	-->
	</script>

	<div id='add_opinion_3979' style='display: none;'>
				
		<div class='row'><label>رای شما :</label>
			<select class='form-control col-md-12' id='opinion_note_3979' name='opinion_note_3979'>
				<option value='0'>بدون امتیاز</option>
				<option value='1'>بد</option>
				<option value='2'>ضعیف</option>
				<option value='3' selected='selected'>خوب</option>
				<option value='4'>بسیار خوب</option>
				<option value='5'>جذاب</option>
			</select>
		</div>
	
		<div class='row'><label>موضوع</label><br />
			<input class='form-control col-md-12' type='text' name='subject' id='edit_subject_3979' size='50'/>
		</div>
		<div class='row'>
			<span class='right'><label>شرح نظر شما</label></span>			
			<span class='left'>
				<input value=' B ' name='B' onclick="insert_text('edit_comment_3979','[b]','[/b]')" type='button' class='btn'> 
				<input value=' I ' name='I' onclick="insert_text('edit_comment_3979','[i]','[/i]')" type='button' class='btn'>
				<input value=' U ' name='U' onclick="insert_text('edit_comment_3979','[u]','[/u]')" type='button' class='btn'>
				<input value='http://' name='Url' onclick="insert_text('edit_comment_3979','[url]','[/url]')" type='button' class='btn'>
				<input value='Img' name='Img' onclick="insert_text('edit_comment_3979','[img]','[/img]')" type='button' class='btn'>
				<input value='Code' name='Code' onclick="insert_text('edit_comment_3979','[code]','[/code]')" type='button' class='btn'>
				<input value='Quote' name='Quote' onclick="insert_text('edit_comment_3979','[quote]','[/quote]')" type='button' class='btn'>
			</span>
		</div>		
		<div class='row'>
			<textarea class='form-control col-md-12' name='CMNT' id='edit_comment_3979' cols='60' rows='2'></textarea>
		</div>
      	<div class='row'>
	        <input type='button' class='btn' onclick=" send_opinion(3979);  return false; " value='ارسال'>
		</div>
	</div>

			</div>
		</div></div></blockquote>
</div><!-- closing #aut_details_list_-->
<hr /><center>
<script type='text/javascript'>
<!--
	function test_form(form)
	{

		if (form.page.value > 1)
		{
			alert("تعداد صفحه بیش از حد بالا است!");
			form.page.focus();
			return false;
		}

		if (form.page.value < 1)
		{
			alert("تعداد صفحه خیلی کم است!");
			form.page.focus();
			return false;
		}
		return true;
	}
-->
</script><form name='form' action='' method='post' onsubmit='return test_form(form)'>
<nav aria-label='Page navigation'><ul class='pagination justify-content-end'>
<li class='page-item' data-toggle='tooltip' class='disabled' title='صفحه اول'><a class='page-link' href='#'><span aria-hidden='true'>&rarr;</span></a></li>
<li class='page-item' data-toggle='tooltip' class='disabled' title='صفحه قبلی'><a class='page-link' href='#'><span aria-hidden='true'>&laquo;</span></a></li>
صفحه 1/1
<li class='page-item' data-toggle='tooltip' class='disabled' title='صفحه بعدی'><a class='page-link' href='#'><span aria-hidden='true'>&raquo;</span></a></li>
<li class='page-item' data-toggle='tooltip' class='disabled' title='صفحه آخر'><a class='page-link' href='#'><span aria-hidden='true'>&larr;</span></a></li>
</form>
</ul></nav>
</center></div><!-- closing #aut_details_container -->
</div><!-- closing #aut_details -->
</div><!-- end right panel -->					
						<div class='col-sm-4'>
								
						</div>
					</div></div> <!-- /div id=main -->

					
					<footer class='d-flex flex-wrap justify-content-between align-items-center py-1 my-2 border-top'>						
						
						<div class='col-sm-2'><div class='opac_sel_lang'><span><form method="post" action="index.php" >انتخاب زبان : <select name="lang_sel" onchange="this.form.submit();"><option value='arm'>ارمنی</option><option value='en_uk'>انگلیسی</option><option value='ar_ar'>عربی</option><option value='ir_fa' selected>فارسی </option><option value='kur'>کردی</option></select></form></span></div></div>
	<div class='col-sm-2'>
	<a class="footer_library_name" href="https://library.knu.edu.af/opac/" title="کتابخانه دانشگاه خاتم النبیین (ص)">کتابخانه دانشگاه خاتم النبیین (ص)</a>
		<a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="375b5e554556454e775c594219525342195651">[email&#160;protected]</a> <br/>
		+930787700700 <br/>
		کابل- سرک دارالامان-دانشگاه خاتم النبیین(ص)<br/>
	</div><div class='col-sm-2'><a href='https://knu.edu.af/' target=_blank>درباره ما</a>
<br/><a href="http://www.faralib.ir" title="نرم افزار کتابخانه" target='_blank'>نرم افزار کتابداری پاسارگاد</a></div>		
		<div class='col-sm-2'><h3><span class='bi bi-info-circle-fill'></span>کاربران آنلاین :17</h3><h3><span class='bi bi-info-circle-fill'></span>بازدید روزانه : 2912</h3><h3><span class='bi bi-info-circle-fill'></span>بازدید سالانه : 644130</h3></div></footer> 
		
		<!--contents_band-->		
		</div><!-- /div id=container -->
		<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script type='text/javascript'>init_drag();	//research!!</script> 
		<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'a160ab135fd9f64d',t:'MTc4MzE5NDcyNA=='};var a=document.createElement('script');a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
		</html>
		