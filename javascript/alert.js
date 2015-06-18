(function (){
  var alert = {};
  alert.close = function (child){
    child.parentNode.remove();
  };
  window.alert = alert;
})();
