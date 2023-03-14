public class Entry <K, V> {
    private K key;
    private V value;
  
    public Entry (K key, V value) {
      this.key = key;
      this.value = value;
    }
    public K getKey() {
      return key;
    }
    public V getValue() {
      return value;
    }
  }
  
  
  public class test {
    public static void main(String[] args) {
      Entry <String, Integer> e1 = new Entry<>("제네시스", 20);
      Entry <String, String> e2 = new Entry<>("제네시스", "현대");
      //Entry<int, String> e3 = new Entry<>(30, "계약");
  
      
      System.out.println(e1.getKey() + " "+ e1.getValue());
      System.out.println(e2.getKey()+ " " + e2.getValue());
      
    }
  }