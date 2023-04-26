package airpollutionseoul_q3;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class AirPollutionSeoul_q3_Mapper extends Mapper<Object, Text, Text, Text>{

	Text output_key = new Text();
	Text output_data = new Text();
	boolean is_head = true;

	protected void map(Object key, Text value, Mapper<Object, Text, Text, Text>.Context context)
			throws IOException, InterruptedException {
		// first line is head
		if(is_head)	{
			is_head = false;
			return;
		}
		String tmp = "";
		// read line
		// colums = [time, station_code, item code, value, instrument status]
		String[] colums = value.toString().split(",");
		if (Integer.parseInt(colums[4]) == 0) {
			// output: < time, station_code >
			output_key.set(String.format("< %s, %s >", colums[0], colums[1]));
			// "item code value"
			output_data.set(String.format("%s %s", colums[2], colums[3]));
			context.write(output_key, output_data);
		}

	}
}
