import java.io.*;
import java.util.*;

public class Main {

    public static class Document{
        int num;
        int idx;

        public Document(int num, int idx){
            this.num = num;
            this.idx = idx;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        while (T-->0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            Queue<Document> queue = new LinkedList<>();
            for(int i=0; i<N; i++){
                Document document = new Document(Integer.parseInt(st.nextToken()), i);
                queue.offer(document);
            }
            int cnt = 0;
            while (true){
                Document flagDocument = queue.poll();
                int flagNum = flagDocument.num;
                int size = queue.size();
                boolean flag = true;
                while (size-->0){
                    Document temDocument = queue.poll();
                    int temNum = temDocument.num;
                    if(temNum>flagNum){
                        flag = false;
                    }
                    queue.offer(temDocument);
                }
                if(flag==false)
                    queue.offer(flagDocument);
                else{
                    if(flagDocument.idx==M){
                        bw.write(String.valueOf(cnt+1)+"\n");
                        break;
                    }
                    else{
                        cnt++;
                    }
                }
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}