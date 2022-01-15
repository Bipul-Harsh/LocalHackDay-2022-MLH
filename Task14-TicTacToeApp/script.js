document.addEventListener('click', tellEvent);

var player = true;
player_x_marks = [];
player_o_marks = [];
function tellEvent(x){
    try{
        var id = x.srcElement.id;
        if (player){
            document.getElementById(id).getElementsByClassName('board-button-text')[0].innerHTML = "X";
            update_move('O');
            player_x_marks.push(parseInt(id));
        }
        else{
            document.getElementById(id).getElementsByClassName('board-button-text')[0].innerHTML = "O";
            update_move('X');
            player_o_marks.push(parseInt(id));
        }
        check_move(player)
        player = !player;
    }catch{
        return;
    }
}
function update_move(move){
    document.getElementById('move-info').innerHTML=move;
}
var correct_moves = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
function check_move(player){
    if(player){
        // X player move check if making win
        for (var ind=0; ind<correct_moves.length; ind++){
            var x_win = true;
            for (var i=0; i<correct_moves[ind].length; i++){
                if(player_x_marks.indexOf(correct_moves[ind][i])==-1){
                    x_win = false;
                }
            }
            if(x_win){
                print_declaration("X wins!");
                return;
            }
        }
    }
    else{
        // O player move check if making win
        for (var ind=0; ind<correct_moves.length; ind++){
            var o_win = true;
            for (var i=0; i<correct_moves[ind].length; i++){
                if(player_o_marks.indexOf(correct_moves[ind][i])==-1){
                    o_win = false;
                }
            }
            if(o_win){
                print_declaration("O wins!");
                return;
            }
        }
    }
    if (player_x_marks.length+player_o_marks.length==9){
        print_declaration("Draw!");
    }
}
function print_declaration(message){
    document.getElementById('declaration-container').style.display = "flex";
    document.getElementById('declaration').innerHTML=message;
}
function reset(){
    location.reload();
}