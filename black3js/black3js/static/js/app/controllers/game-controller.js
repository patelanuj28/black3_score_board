Black3js.controller('GameController', function ($scope, $location,  GlobalService, GameService, ScoreService,PlayersService, games) {
    $scope.games = games;

    //console.log($scope.games.players);
    if(games.players){
        $.each($scope.games.players, function( index, value ) {
            total = 0;        
            value['total_scores'] = 0
            $.each(value.scores, function(ind1, val1){
                if(!isNaN(val1.score)) {
                    value['total_scores'] += parseInt(val1.score);
                }
            });
        });
    }

//    console.log($scope.games);
    
    $scope.globals = GlobalService;
    //options for modals
    $scope.opts = {
        backdropFade: true,
        dialogFade: true
    };
    //open modals
    $scope.open1 = function (action) {
        if (action === 'create'){
            $scope.gameModalCreate = true;
            $scope.game = new Object();
        };
    };
    $scope.getTotalCards = function(num){
        return (52 - (52 % num));
    }
    $scope.getIndividualCards = function(num){
        return ((52 - (52 % num)) / num);   
    }
    $scope.getNumber = function(num) {
        return new Array(num);
    };

    //close modals
    $scope.close1 = function (action) {
        if (action === 'create'){
            $scope.gameModalCreate = false;
        };
    };
    //calling board service
    $scope.create = function () {

        GameService.save($scope.game).then(function (data) {
            $scope.game = data;
            $scope.games.push(data);
            $scope.gameModalCreate = false;
        }, function(status){
            console.log(status);
            $scope.gameModalCreate = false;
        });
    };

    /*$scope.$watch('games', function() {
        $scope.games = return GameService.list();
    }); */

    var failureCb = function (status) {
        console.log(status);
    }
    //options for modals
    $scope.opts = {
        backdropFade: true,
        dialogFade: true
    };
    //open modals
    $scope.open = function (action) {
        $scope.gameTotalPlayers = $scope.games.total_players;
        if (action === 'edit'){
            $scope.gameModalEdit = true;
        };
    };
    //close modals
    $scope.close = function (action) {
        $scope.gameTotalPlayers = "";

        if (action === 'edit'){
            $scope.gameModalEdit = false;
        };
    };
    //calling board service
    $scope.update = function () {
        GameService.update($scope.games).then(function (data) {
            $scope.games = data;
            $scope.gameModalEdit = false;
        }, failureCb);
    };

    $scope.delete = function (game_id) {
        var res=confirm('Are you sure you want to delete game '+ game_id+'?');
        if (res == false)
            return;

        GameService.remove(game_id).then(function (data) {
            $scope.games = GameService.list();            
        }, failureCb);
    };

    $scope.addPlayer = function() {
        $scope.number = $scope.games.total_players;
        $scope.game_id = $scope.games.id;

        //if ($scope.totalPlayers > 1 && $scope.totalPlayers < 13){
            //$location.path('/Player/'+$scope.totalPlayers);
        //}
        $scope.player_name = [];
        var pattern = /^[a-zA-Z]+/
        $('input[name="player[]"]').each(function(){

            if($(this).val() == '' && !pattern.test($(this).val())){

                $scope.player_name.push($(this).val());
                $scope.error = 'Player name should not be empty';
            }else{
                $scope.error = ''
            }
            $scope.player_name.push($(this).val());
        });
        if ($scope.error == ''){

            $.each($scope.player_name, function( index, value ) {
                data = {game: $scope.game_id, name: value};
                PlayersService.save(data).then(function (data) {
                    $location.path('/');
                    
                }, function(status){
                    console.log(status);
                    $location.path('/');
                   
                });
            });
            
                
            
        
        }

    };

    $scope.addScore = function() {
        $scope.game_id = $scope.games.id;

        //if ($scope.totalPlayers > 1 && $scope.totalPlayers < 13){
            //$location.path('/Player/'+$scope.totalPlayers);
        //}
        
        var pattern = /^[a-zA-Z]+/
        var player_score = [];
        $scope.error = false;
        $('input[type="text"]').each(function(index){            
            if($(this).val() == ''){
                $scope.error = true;
            }else{
                player_score[index] = { id: $(this).attr('name'), score: $(this).val()};
                //player_score[index]['score'] = $(this).val();                
            }
            
            
        });
        if($scope.error == false){
            $.each(player_score, function(index, value){
                var data = {};
                data={score: value.score, name: value.id, game:$scope.game_id};


                    ScoreService.save(data).then(function (data) {
                        $location.path('/score/'+$scope.game_id+'/');
                        
                    }, function(status){
                        console.log(status);
                        $location.path('/score/'+$scope.game_id+'/');
                       
                    });
                });
        }
                
                
            
        
        

    };


});