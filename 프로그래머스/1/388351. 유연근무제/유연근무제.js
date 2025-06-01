function solution(schedules, timelogs, startday) {
    var answer = 0;
    let n = schedules.length;
    let nn = timelogs[0].length;
    var result = Array(n).fill(true);
    var sche = []
    for (let i=0; i<n;i++) {
        var hh = parseInt(schedules[i]/100);
        var mm = (schedules[i]%100)+10;
        if (mm >= 60) {
            mm -= 60
            hh += 1
        }
        let clock = hh*100+mm;
        sche.push(clock)
    }
    
    for (let i = 0; i <nn; i++ ) {
        for (let j=0; j<n; j++) {
            if (result[j] === true && startday <= 5) {                
                if (sche[j] < timelogs[j][i]) {
                    result[j] = false
                }
            }
        }
        startday = (startday%7)+1;
    }
    
    for (let i = 0; i<n; i++ ) {
        if (result[i] === true) {
            answer += 1;
        }
        
    }
    return answer;
}