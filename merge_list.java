
import java.util.*;

public class merge_list {
	public static void main(String[] args) {
		String[] original = {"one", "two", "three"};
		String[] to_add = {"one", "two", "five", "six"};
		String[] to_del = {"two", "five"};	
		String[] result = modified(original, to_add, to_del);
		for (int i = 0; i < result.length; i++) {
			System.out.print(result[i] + " ");
		}
		System.out.println("");
	}

	final static String[] modified(String[] original, String[] to_add, String[] to_del) {
		String[] merged = new String[original.length + to_add.length];
		int count = 0;
		for (int i = 0; i < original.length; i++) {
			merged[count] = original[i];
			count++;
		}
		for (int i = 0; i < to_add.length; i++) {
			merged[count] = to_add[i];
			count++;
		}
		
		List<String> arr = new ArrayList<String>();
		List<String> arr_to_del = new ArrayList<String>();
		for (int i = 0; i < merged.length; i++) {
			arr.add(merged[i]);
		}
		for (int i = 0; i < to_del.length; i++) {
			arr_to_del.add(to_del[i]);
		}
		
		arr.removeAll(arr_to_del);
		System.out.println("arr: " + arr.toString());

		Set<String> nodup = new HashSet<String>();
		nodup.addAll(arr);

		String[] result = new String[nodup.size()];
		count = 0;
		Iterator<String> it = nodup.iterator();
		while(it.hasNext()) {
			result[count] = it.next();
			count++;
		}

		Arrays.sort(result, new Comparator<String>() {
			@Override
			public int compare(String str1, String str2) {
				if (str1.length() == str2.length()) {
					return str2.charAt(0) - str1.charAt(0);
				}
				return str2.length() - str1.length();
			}
		});
		return result;
	}
}


