import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class JobQueue {
    // number of threads
    private int numWorkers;
    private int[] jobs;

    private int[] assignedWorker;
    private long[] startTime;

    private FastScanner in;
    private PrintWriter out;

    public static void main(String[] args) throws IOException {
        new JobQueue().solve();
    }

    private void readData() throws IOException {
        numWorkers = in.nextInt();
        int m = in.nextInt();
        jobs = new int[m];
        for (int i = 0; i < m; ++i) {
            jobs[i] = in.nextInt();
        }
    }

    private void writeResponse() {
        for (int i = 0; i < jobs.length; ++i) {
            out.println(assignedWorker[i] + " " + startTime[i]);
        }
    }

    private void siftDown(int i, ArrayList<Thread> nextFreeTime) {
        int minIndex = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (right < numWorkers && (nextFreeTime.get(minIndex).startingTime > nextFreeTime.get(right).startingTime
                || (nextFreeTime.get(minIndex).startingTime == nextFreeTime.get(right).startingTime) &&
                (nextFreeTime.get(minIndex).id > nextFreeTime.get(right).id))) {
            minIndex = right;
        }
        if (left < numWorkers && (nextFreeTime.get(minIndex).startingTime > nextFreeTime.get(left).startingTime
                || (nextFreeTime.get(minIndex).startingTime == nextFreeTime.get(left).startingTime) &&
                (nextFreeTime.get(minIndex).id > nextFreeTime.get(left).id))) {
            minIndex = left;
        }
        if (minIndex != i) {
            Thread tmp = nextFreeTime.get(minIndex);
            nextFreeTime.set(minIndex, nextFreeTime.get(i));
            nextFreeTime.set(i, tmp);

            siftDown(minIndex, nextFreeTime);
        }
    }


    private void assignJobs() {
        // TODO: replace this code with a faster algorithm.
        assignedWorker = new int[jobs.length];
        startTime = new long[jobs.length];
        ArrayList<Thread> nextFreeTime = new ArrayList<Thread>();
        
        // initialize nextFreeTime
        for (int i = 0; i < numWorkers; i++) {
            nextFreeTime.add(new Thread(i, 0));
        }
        for(int i = 0; i < jobs.length; i++) {
            int duration = jobs[i];
            assignedWorker[i] = nextFreeTime.get(0).id;
            startTime[i] = nextFreeTime.get(0).startingTime;
            nextFreeTime.get(0).startingTime += duration;
            //threadHeap(nextFreeTime);
            siftDown(0, nextFreeTime);
        }
    }

    public void solve() throws IOException {
        in = new FastScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        readData();
        assignJobs();
        writeResponse();
        out.close();
    }

    static class FastScanner {
        private BufferedReader reader;
        private StringTokenizer tokenizer;

        public FastScanner() {
            reader = new BufferedReader(new InputStreamReader(System.in));
            tokenizer = null;
        }

        public String next() throws IOException {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                tokenizer = new StringTokenizer(reader.readLine());
            }
            return tokenizer.nextToken();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }

    static class Thread {
        private int id;
        private long startingTime;

        public Thread(int id, long startingTime) {
            this.id = id;
            this.startingTime = startingTime;
        }

        public Thread(Thread newThread) {
            this.id = newThread.id;
            this.startingTime = newThread.startingTime;
        }
    }
}
