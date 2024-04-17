import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        String[] arr = new String[N];
        for(int i=0; i<N; i++){
            arr[i] = br.readLine();
        }

        int len = 1;
        while (true){
            boolean flag = true;
            HashMap<String, Integer> map = new HashMap<>();
            for(int i=0; i<N; i++){
                String tem = arr[i].substring(arr[i].length()-len,arr[i].length());
                if(map.containsKey(tem)){
                    flag = false;
                    break;
                }
                else{
                    map.put(tem, 1);
                }
            }
            if(flag==false){
                len++;
            }
            else{
                bw.write(String.valueOf(len));
                break;
            }

        }

        bw.flush();
        bw.close();
        br.close();
    }
}