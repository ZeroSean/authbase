var sy = sy || {};

$.extend(Highcharts.getOptions().lang, {
	printChart : '打印图表',
	downloadPNG : '下载 PNG 图片',
	downloadJPEG : '下载 JPEG 图片',
	downloadPDF : '下载 PDF 文档',
	downloadSVG : '下载 SVG vector image',
	contextButtonTitle : '导出菜单'
});
$.extend(Highcharts.getOptions().exporting, {
	filename : 'chart',
	url : sy.contextPath + '/downloadChart',
	sourceWidth: 1200,
	sourceHeight: 400,                
	chartOptions: {
		xAxis: [{
			min: 0,
			max: 28
		}]
	}
});
$.extend(Highcharts.getOptions(), {
	credits : {
		enabled : false
	}
});