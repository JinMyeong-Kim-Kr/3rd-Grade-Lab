package airpollutionseoul_q3;

import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class AirPollutionSeoul_q3_Reducer extends Reducer<Text, Text, Text, Text>{

	Text output_key = new Text();
	Text output_text = new Text();

	protected void reduce(Text key, Iterable<Text> values,
			Reducer<Text, Text, Text, Text>.Context context) throws IOException, InterruptedException {

		String text = "";

		for(Text value : values) {
			String[] col = value.toString().split(" ");
			switch (Integer.parseInt(col[0])){
				// SO2
				case 1:
					text += "SO2 = " + col[1] + ", ";
					break;
				// NO2
				case 3:
					text += "NO2 = " + col[1] + ", ";
					break;
				// CO
				case 5:
					text += "CO = " + col[1] + ", ";
					break;
				// O3
				case 6:
					text += "O3 = " + col[1] + ", ";
					break;
				// PM10
				case 8:
					text += "PM10 = " + col[1] + ", ";
					break;
				// PM2.5
				case 9:
					text += "PM2.5 = " + col[1] + ", ";
					break;
			}
		}
		output_key.set(key);
		output_text.set(text);
		context.write(output_key, output_text);
		
	}

}
