package airpollutionseoul_q2;

import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class AirPollutionSeoul_q2_Reducer extends Reducer<Text, IntWritable, Text, Text>{

	Text output_key = new Text();
	Text output_text = new Text();

	int max_total_data = 0;
	String max_key = "";

	protected void reduce(Text key, Iterable<IntWritable> values,
			Reducer<Text, IntWritable, Text, Text>.Context context) throws IOException, InterruptedException {

		int total_data = 0;

		for(IntWritable cnt : values) {
			total_data += cnt.get();
		}
		output_key.set("station code = " + key);
		output_text.set(String.format("count = %d", total_data));
		context.write(output_key, output_text);
		
	}

}
