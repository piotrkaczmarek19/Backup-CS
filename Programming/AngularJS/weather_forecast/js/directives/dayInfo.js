app.directive('forecast', function(){

    return{
        restrict: 'E',
        scope:{
            info:"="
        },
        templateUrl: 'js/directives/dayInfo.html'

    };

});
