var sy = sy || {};

/**
 * 去字符串空格
 * 
 * @author Jeffrey
 */
sy.trim = function(str) {
	return str.replace(/(^\s*)|(\s*$)/g, '');
};
sy.ltrim = function(str) {
	return str.replace(/(^\s*)/g, '');
};
sy.rtrim = function(str) {
	return str.replace(/(\s*$)/g, '');
};

/**
 * 判断开始字符是否是XX
 * 
 * @author Jeffrey
 */
sy.startWith = function(source, str) {
	var reg = new RegExp("^" + str);
	return reg.test(source);
};
/**
 * 判断结束字符是否是XX
 * 
 * @author Jeffrey
 */
sy.endWith = function(source, str) {
	var reg = new RegExp(str + "$");
	return reg.test(source);
};

/**
 * iframe自适应高度
 * 
 * @author Jeffrey
 * 
 * @param iframe
 */
sy.autoIframeHeight = function(iframe) {
	iframe.style.height = iframe.contentWindow.document.body.scrollHeight + "px";
};

/**
 * 设置iframe高度
 * 
 * @author Jeffrey
 * 
 * @param iframe
 */
sy.setIframeHeight = function(iframe, height) {
	iframe.height = height;
};