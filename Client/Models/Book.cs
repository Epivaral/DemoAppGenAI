using System.Net.Http.Json;

namespace Client.Models
{
    public class Book
    {
        public int BookID { get; set; }
        public string Title { get; set; }
        public string Author { get; set; }
        public string Genre { get; set; }
        public string ReadStatus { get; set; }
        public string Description { get; set; }
    }
}
