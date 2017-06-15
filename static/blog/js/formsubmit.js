function success(){
	alertbox();
	{% load static %}
	window.location.href="{% static '..' %}";
	alertbox();
}
/*無法新增至資料庫*/

function alertbox() {
	alert("留言提交成功！\n\n點擊「OK」後，系統將重新導入頁面...");
}