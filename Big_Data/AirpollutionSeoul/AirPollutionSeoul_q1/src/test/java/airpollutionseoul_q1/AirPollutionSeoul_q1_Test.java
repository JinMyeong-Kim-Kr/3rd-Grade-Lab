package airpollutionseoul_q1;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.util.ToolRunner;

public class AirPollutionSeoul_q1_Test {
	public static void main(String[] args) throws Exception {
		
		Configuration conf = new Configuration();
		conf.setInt("mapreduce.job.reduces", 3);
		
		String[] input_args = {"src/test/resources/seoul.csv"};
		ToolRunner.run(conf, new AirPollutionSeoul_q1(), input_args);
	}
}
