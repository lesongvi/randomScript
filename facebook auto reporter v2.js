var macro; 
var ids=prompt("Reporting IDS File (.csv)","C:\\ids.csv" );
var amount=prompt("IDs Amount " , "e.g : 10");
var id=0;


var path=prompt("Reporting-Link's File Path (.csv)","C:\\report.csv" );

var links=prompt("Reports links " , "e.g : 10");
var l=links;

while (amount>0){
var wait=0,i=0;
macro =  "CODE:";
macro +="SET !TIMEOUT_STEP 5"+ "\n";
macro +="SET !ERRORIGNORE YES" + "\n";
macro +="SET !DATASOURCE "+ids +""+ "\n";
id++;
macro +="SET !DATASOURCE_COLUMNS 2" + "\n";
var id_loop= "SET !DATASOURCE_LINE " + id ;
macro +=id_loop+ "\n";

macro +=  "URL GOTO=https://mbasic.facebook.com/" + "\n";
macro +="wait seconds=2" + "\n";
macro +=  "TAG POS=1 TYPE=INPUT:TEXT FORM=ID:login_form ATTR=NAME:email CONTENT={{!col1}}" + "\n";
macro +="wait seconds=1" + "\n";
macro +=  "SET !ENCRYPTION NO" + "\n";
macro +=  "TAG POS=1 TYPE=INPUT:PASSWORD FORM=ID:login_form ATTR=NAME:pass CONTENT={{!col2}}" + "\n";
macro +="wait seconds=2" + "\n";
macro +=  "TAG POS=1 TYPE=INPUT:SUBMIT FORM=ID:login_form ATTR=NAME:login" + "\n";
macro +="wait seconds=4" + "\n";






while (l>0){
if (l>70){
	alert ("Links are too much and can be risky !\n Reduce links to min:50");
	break;
}else if(l==0){
	alert ("Invalid Links Count");
	break;
}

macro +="SET !TIMEOUT_STEP 5"+ "\n";
macro +="SET !ERRORIGNORE YES" + "\n";
macro +="SET !DATASOURCE "+path +""+ "\n";
i++;
macro +="SET !DATASOURCE_COLUMNS 1" + "\n";
var loop="SET !DATASOURCE_LINE " + i ;
macro +=loop+ "\n";
macro +="URL GOTO={{!col1}}" + "\n";
macro +="wait seconds=1" + "\n";
macro +="TAG POS=1 TYPE=SPAN ATTR=TXT:Submit<SP>to<SP>Facebook<SP>for<SP>Review"+ "\n";
macro +="wait seconds=1"+ "\n";
macro +="TAG POS=1 TYPE=INPUT:SUBMIT FORM=ID:actions-form ATTR=*"+ "\n";
if (wait == 5 ){
	if (links<10){
	macro +="wait seconds=100" + "\n"; 
	wait=0;
	}else if (links>10 || links<=20){
		if (l>0 || l<10){
		macro +="wait seconds=200" + "\n"; 
		wait=0;
		}else if (l>10 || l<=20){
		macro +="wait seconds=100" + "\n"; 
		wait=0;
		} 
	
	}else if (links>20 || links<=35){
		if (l>0 || l<10){
		macro +="wait seconds=350" + "\n"; 
		wait=0;
		}else if (l>10 || l<=20){
		macro +="wait seconds=280" + "\n"; 
		wait=0;
		} else if (l>20 || l<25){
		macro +="wait seconds=200" + "\n"; 
		wait=0;
		} else if (l>25 || l<=35){
		macro +="wait seconds=100" + "\n"; 
		wait=0;
		} 
	}
	else {
		if (l>0 || l<5){
		macro +="wait seconds=250" + "\n"; 
		wait=0;
		}else if (l>5 || l<=15){
		macro +="wait seconds=380" + "\n"; 
		wait=0;
		} else if (l>15 || l<20){
		macro +="wait seconds=350" + "\n"; 
		wait=0;
		} else if (l>20 || l<=35){
		macro +="wait seconds=300" + "\n"; 
		wait=0;
		} else if (l>35 || l<40){
		macro +="wait seconds=280" + "\n"; 
		wait=0;
		} else if (l>40 || l<50){
		macro +="wait seconds=200" + "\n"; 
		wait=0;
		} else {
		macro +="wait seconds=90" + "\n"; 
		wait=0;
		} 
	}
}else {
macro +="wait seconds=3" + "\n";
}
wait++;
l--;

}
l=links;
wait=0;
macro +=  "URL GOTO=https://facebook.com/" + "\n";
macro +=  "wait seconds=2" + "\n";
macro +=  "TAG POS=1 TYPE=DIV ATTR=ID:userNavigationLabel" + "\n";
macro +=  "wait seconds=3" + "\n";
macro +=  "TAG POS=2 TYPE=SPAN ATTR=TXT:Log<SP>out" + "\n";
ret=iimPlay(macro);

if (ret==-101){
	break;
}

amount--;
}
