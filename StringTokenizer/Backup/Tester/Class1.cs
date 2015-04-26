using System;
using System.IO;

using Ader.Text;

namespace Tester
{
	/// <summary>
	/// Summary description for Class1.
	/// </summary>
	class Class1
	{
		/// <summary>
		/// The main entry point for the application.
		/// </summary>
		[STAThread]
		static void Main(string[] args)
		{
			if (args.Length == 0)
				TestConsoleInput();
			else if (args.Length == 1)
			{
				TestFromFile(args[0]);
			}


		}

		public static void TestFromFile(string filename)
		{
			StreamReader reader = null;
			try
			{
				reader = new StreamReader(filename);

				StringTokenizer tok = new StringTokenizer(reader);

				Token token;
				do
				{
					token = tok.Next();
					Console.WriteLine("{0} at {1}, {2}: {3}", token.Kind.ToString(), token.Line, token.Column, token.Value);

					if (token.Kind == TokenKind.EOL)
					{
						Console.WriteLine("--------------------------------------------");
					}
						
				} while (token.Kind != TokenKind.EOF);

			}
			catch (IOException e)
			{
				Console.WriteLine("IO Error:" + e.Message);
			}
			finally 
			{
				if (reader != null)
					reader.Close();
			}
				

		}

		public static void TestConsoleInput()
		{

			Console.WriteLine("Type 'exit' to quit.");

			while (true)
			{
				Console.Write(">");
				string input = Console.ReadLine();
				if (string.Compare(input, "exit", true)==0)
					break;

				StringTokenizer tok = new StringTokenizer(input);

				Token token;
				do
				{
					token = tok.Next();
					Console.WriteLine("{0} at {1}, {2}: {3}", token.Kind.ToString(), token.Line, token.Column, token.Value);
						
				} while (token.Kind != TokenKind.EOF);

			}
		}
	}
}
