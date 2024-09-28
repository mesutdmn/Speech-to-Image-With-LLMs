iframe = window.parent.document.querySelector('iframe');
iframeDocument = iframe.contentWindow.document;
const stopButton = iframeDocument.querySelector('#stop');
const recordButton = iframeDocument.querySelector('#record');

const canvasElement = iframeDocument.querySelector('.audio-react-recorder__canvas');
const downButton = iframeDocument.querySelector('#continue');
const resetButton = iframeDocument.querySelector('#reset');
const audio = iframeDocument.querySelector('#audio');
infobox = window.parent.document.querySelectorAll('[data-testid="stAlertContentInfo"]')[2]
const p_infobox = infobox.querySelector('p')

streamlit_buttons = window.parent.document.querySelectorAll('[kind="secondary"]')

canvasElement.style.display = 'none';
resetButton.style.display = 'none';
downButton.style.display = 'none';
audio.style.display = 'none';
stopButton.style.display = 'none';
iframe.style.height = '74px'
recordButton.addEventListener('click', startRecord);
stopButton.addEventListener('click', stopRecord);

function startRecord(){
	recordButton.style.display = 'none';
	stopButton.style.display = 'inline-block';
	iframe.style.height = '50px'
	p_infobox.innerText = '🎤 Recording..'
};

function stopRecord(){
	recordButton.style.display = 'inline-block';
	stopButton.style.display = 'none';
	iframe.style.height = '74px'
	p_infobox.innerText = '✅ Record is done!'
};