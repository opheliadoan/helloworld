/* BaseballElimination.java
 * CSC 226 - Spring 2019
 * Assignment 4 - Baseball Elimination Program
 * 
 * This template includes some testing code to help verify the implementation
 * To interactively provide test inputs, run the program with java BaseballEliminatiion
 * To conveniently test the algorithm with a large input, create a text file containing
 *  one or more test divisions (in the format described below) and run the program with
 * java -cp .;algs4.jar BaseballElimination file.txt (Windows)
 * or 
 * java -cp .:algs4.jar BaseballElimation file.txt (Linus or Mac)
 * where file.txt is replaced by the name of the text file.
 * The input consists of an integer representing the number of teams in the division and then
 * for each team, the team name (no whitespace), number of wins, number of losses, and a list 
 * of integers representing the number of games remaining against each team (in oder from the 
 * first team to the last).
 * That is, the text file looks like:
 * <number of teams in division>
 * <team1_name wins losses games_vs_team1 games_vs_team2 ... gaems_vs_teamn>
 * ...
 * <teamn_name wins losses gaems_vs_team1 games_vs_team2 ... games_vs_teamn>
 * An input file can contain an unlimited number of divisions but all team names are unique,
 *  i.e. no team can be in more than one division.
 * 
 * R.Little - 03/22/2019
 */

import edu.princeton.cs.algs4.*;
import java.util.*;
import java.io.File;

//Do not change the name of the BaseballElimination class
public class BaseballElimination {
    
    //We use an ArrayList to keep track of the eliminated teams.
    public ArrayList<String> eliminated = new ArrayList<String>();
    
    private int numTeams;
    private int vertices;
    private double total_games_left;
    private int [] wins;
    private int [] games_left;
    private double [][] againstGames;
    private String [] teamNames;
    private boolean[] alreadyElim;
    
    /* BaseballElimination(s) 
     * Given an input stream connected to a collection of baseball division 
     * standings we determine for each division which teams have been eliminated 
     * from the playoffs. For each team in each division we create a flow network 
     * to determine the maxflow in that network. If the maxflow exceeds the number
     * of inter-divisional games between all other teams in the division, 
     * the current team is eliminated
     */
    public BaseballElimination(Scanner s) {
        
        /* ... Your code here ... */
        //read input
        numTeams = s.nextInt();
        
        this.vertices = (numTeams*numTeams - numTeams + 4)/2;
        
        wins = new int[numTeams];
        teamNames = new String[numTeams];
        games_left = new int[numTeams];
        alreadyElim = new boolean[numTeams];
        
        againstGames = new double[numTeams][numTeams]; 
        
        int i = 0;
        while(s.hasNext()) {
            teamNames[i] = s.next();
            wins[i] = s.nextInt();
            games_left[i] = s.nextInt();
            for (int j = 0; j < numTeams; j++) {
                againstGames[i][j] = s.nextInt();
            }
            i++;
        }
        
        //check the easiest case
        for (int x = numTeams - 1; x >= 0; x--) {
            alreadyElim[x] = trivialCaseElim(x);
        }
        
        for (int x = numTeams - 1; x >= 0; x--) {
            if (!alreadyElim[x]) {
                this.total_games_left = 0;
                FlowNetwork G = buildFlowNetwork(x);
                alreadyElim[x] = harderCaseElim(G, x);
            }
        }

        for (int k = 0; k < alreadyElim.length; k++) {
            if (alreadyElim[k]) {
                eliminated.add(teamNames[k]);
            }
        }

    }
    
    //trivial case: remove team whose wins + games_left < wins of some team
    private boolean trivialCaseElim(int team) {
        for (int i = 0; i < numTeams; i++) {
            if (i != team) {
                if (wins[team] + games_left[team] < wins[i]) {
                    return true;
                }
            }
        }
        return false;
    }
    
    //harder case
    private boolean harderCaseElim(FlowNetwork flowNetwork, int team) {
        
        FordFulkerson maxflow = new FordFulkerson(flowNetwork, 0, vertices - 1);
        double maxValue = maxflow.value();
        // if (team == 3) {

        //     System.out.println(teamNames[team] + ": ");
        //     System.out.println(flowNetwork.toString());
        //     System.out.println(maxValue);
        //     System.out.println(total_games_left);
        // }
        if (maxValue < total_games_left) {
            return true;
        }
        return false;
    }
    
    private FlowNetwork buildFlowNetwork(int team) {
        FlowNetwork flowNetwork = new FlowNetwork(vertices); 
        int s = 0;
        int t = this.vertices - 1;
        int W = wins[team] + games_left[team];
        
        int counter = 1;
        int numMatches = numberOfMatches();
        
        int[] id = new int[numTeams];
        int temp = 1;
        for (int i = 0; i < id.length; i++) {
            if (i != team) {
                //id[i] = numMatches + 1 + i;
                id[i] = numMatches + numTeams - temp - i;
            } else {
                id[i] = 0;
                temp = 0;
            }
        }
        
        //build flow network 
        for (int i = 0; i < numTeams - 1; i++) {
            if (i != team) {
                for (int j = i + 1; j < numTeams; j++) {
                    if (j!= team) {
                        flowNetwork.addEdge(new FlowEdge(s, counter, againstGames[i][j]));
                        total_games_left += againstGames[i][j]; 
                        flowNetwork.addEdge(new FlowEdge(counter, id[i], Double.MAX_VALUE));
                        flowNetwork.addEdge(new FlowEdge(counter, id[j], Double.MAX_VALUE));
                        counter++;
                    }
                }
                flowNetwork.addEdge(new FlowEdge(id[i], t, W - wins[i]));
            }
        }
        if (numTeams - 1 != team) {
            flowNetwork.addEdge(new FlowEdge(id[numTeams - 1], t, W - wins[numTeams - 1]));
        }
        return flowNetwork;
    }


    public int numberOfTeams() {
        return this.numTeams;
    }
    
    public int numberOfMatches() {
        return (this.numTeams - 1)*(this.numTeams - 2)/2;
    }
    
    public void teamNames() {
        System.out.printf("[");
        for (int i = 1; i <= numTeams; i++) {
            if (i < numTeams) {
                System.out.printf(teamNames[i - 1] + ", ");
            } else {
                System.out.println(teamNames[i - 1] + "]");
            }
        }
    }
    
    /* main()
     * Contains code to test the BaseballElimation function. You can modify the testing
     * code if needed, but nothing in this function will be considered during marking, 
     * and the testing process used for marking will not execute any of the code below.
     */
    public static void main(String[] args) {
        Scanner s;
        if (args.length > 0) {
            try {
                s = new Scanner(new File(args[0]));
            } catch (java.io.FileNotFoundException e) {
                System.out.printf("Unable to open %s.\n",  args[0]);
                return;
            }
            System.out.printf("Reading input values %s.\n", args[0]);
        } else {
            s = new Scanner(System.in);
            System.out.printf("Reading input values from stdin.\n");
        }
        
        BaseballElimination be = new BaseballElimination(s);
        be.teamNames();
        if (be.eliminated.size() == 0) {
            System.out.println("No team have been eliminated.");
        } else {
            System.out.println("Teams eliminated: " + be.eliminated);
        }
    }

}
