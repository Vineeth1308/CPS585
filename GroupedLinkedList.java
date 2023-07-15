
import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.function.IntPredicate;
import java.util.function.Predicate;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class GroupedLinkedList {

    public static void main(String[] args) {
        List<String> list = Arrays.asList("Geeks", "for",
                "GeeksQuiz", "GeeksforGeeks", "GFG");

        List<Integer> list2 = Arrays.asList(1,2,3,4);

        List<Integer> list3 = Arrays.asList(22,34,45,65);

        System.out.println("The sorted stream is : ");

        // displaying the stream with elements
        // sorted in their natural order
        Stream.of(list,list2,list3).flatMap(Collection::stream).forEach(System.out::println);
        //list.stream().sorted().flatMap(list1-> list2.stream()).forEach(System.out::println);
    }
}
