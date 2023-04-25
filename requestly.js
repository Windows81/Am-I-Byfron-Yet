window.navigator.msLaunchUri = (url) => {
	console.log(666);
	const iframe = document.createElement("iframe");
	iframe.id = "gamelaunch";
	iframe.className = "hidden";
	iframe.src = url
		.replace(/robloxLocale:.._../, "robloxLocale:en_us")
		.replace(/gameLocale:.._../, "gameLocale:en_us")
		.replace(/channel:[^\+]*/, "channel:");
	debugger;
	document.getElementsByTagName("body")[0].append(iframe);
};
