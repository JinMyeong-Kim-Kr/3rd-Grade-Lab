package airpollutionseoul_q4;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.util.ToolRunner;

public class AirPollutionSeoul_q4_Test {
	public static void main(String[] args) throws Exception {
		
		Configuration conf = new Configuration();
		conf.setInt("mapreduce.job.reduces", 3);
		
		String[] input_args = {"src/test/resources/seoul.csv"};
		ToolRunner.run(conf, new AirPollutionSeoul_q4(), input_args);
	}
}
