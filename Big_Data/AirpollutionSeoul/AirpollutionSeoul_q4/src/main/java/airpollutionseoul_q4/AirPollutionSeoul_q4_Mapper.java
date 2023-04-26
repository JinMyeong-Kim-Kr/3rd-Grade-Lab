package airpollutionseoul_q4;

import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class AirPollutionSeoul_q4_Mapper extends Mapper<Object, Text, Text, Text>{

	Text output_key = new Text();
	Text output_value = new Text();

	boolean is_head = true;

	protected void map(Object key, Text value, Mapper<Object, Text, Text, Text>.Context context)
			throws IOException, InterruptedException {
		// first line is head
		if(is_head)	{
			is_head = false;
			return;
		}

		// colums = [time, station_code, item code, value, instrument status]
		String[] colums = value.toString().split(",");
		// time = [date, time]
		String[] time = colums[0].split(" ");
		if (Integer.parseInt(colums[4]) == 0) {
			output_key.set(time[1]);
			output_value.set(String.format("%s %s", colums[2], colums[3]));
			context.write(output_key, output_value);
		}
	}
}
