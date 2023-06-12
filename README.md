<h1>Network Port Scanner (Proof of Concept)</h1>

This Python utility allows you to scan a range of ports on a target host to determine if they are open or closed. It provides a quick way to identify potential entry points for attackers and assess the security of a networked system.

<h2>How It Works</h2>
1. You specify the target host (e.g., a domain or IP address) and the range of ports you want to scan.

2. The utility uses multiple threads to perform concurrent port scanning, making the process faster and more efficient.

3. For each port in the specified range, the utility attempts to establish a TCP connection to the target host on that port.

4. If the connection is successful, the port is considered <b>open</b>, indicating that there is a service or application listening on that port.

5. If the connection fails, the port is considered <b>closed</b>, meaning that there is no service actively listening on that port.

6. The utility displays the results of the port scanning process, indicating which ports are open and which ports are closed.

<h2>How to Use</h2>
1. Clone or download the repository to your local machine.

2. Install Python if you haven't already.

3. Open the port_scanner.py file in a text editor.

4. Customize the target_host, start_port, and end_port variables in the main section of the script to match your desired scanning parameters.

5. Save the changes.

6. Open a terminal or command prompt and navigate to the directory where the script is located.

7. Run the following command to execute the port scanner:

<b><pre>python port_scanner.py</pre></b>

8. Wait for the scanning process to complete. The utility will display the status of each port in the specified range, indicating whether it is open or closed.

9. Analyze the results to gain insights into the security of the target host and identify potential vulnerabilities.

<h2>Customization</h2>
You can customize the target host and port range in the script to match your specific requirements. For example, you can scan a single host, multiple hosts, or a different range of ports. Feel free to modify the script and add additional functionality as needed.

<h1>Legal Disclaimer for Port Scanner (Proof of Concept)</h2>

Please read the following disclaimer carefully before using the Port Scanner Proof of Concept ("the tool") developed by Jacob Dornbusch ("the author"). By using the tool, you agree to be bound by the terms and conditions stated herein.

<b>Lawful Use:</b> The Port Scanner Proof of Concept is provided for informational and educational purposes only. It is designed to assist in identifying open ports on networks with proper authorization. It is crucial to understand that you must use the tool in compliance with all applicable laws, regulations, and ethical guidelines. The author expressly disclaims any responsibility for any misuse of the tool for illegal activities.

<b>Authorized Networks:</b> You should only use the Port Scanner Proof of Concept on networks for which you have obtained written consent from the appropriate network owner or administrator. Unauthorized network scanning is strictly prohibited and may be subject to civil and criminal penalties.

<b>No Liability:</b> The author, Jacob Dornbusch, shall not be held responsible for any damages, losses, or liabilities arising from the use or misuse of the Port Scanner Proof of Concept. This includes but is not limited to any direct, indirect, incidental, special, or consequential damages, loss of data, or financial loss.

<b>No Warranty:</b> The Port Scanner Proof of Concept is provided "as is" and without any warranty, express or implied. The author does not guarantee the accuracy, reliability, or suitability of the tool for any specific purpose. The author disclaims all warranties, including but not limited to warranties of merchantability, fitness for a particular purpose, and non-infringement.

<b>User Responsibility:</b> You are solely responsible for your use of the Port Scanner Proof of Concept. It is your responsibility to ensure that your use of the tool complies with all applicable laws and regulations. You acknowledge that you are using the tool at your own risk.

<b>Indemnification:</b> You agree to indemnify and hold harmless the author, Jacob Dornbusch, from any claims, demands, liabilities, costs, or expenses, including reasonable attorney fees, arising out of or related to your use or misuse of the Port Scanner Proof of Concept.

By using the Port Scanner Proof of Concept, you acknowledge that you have read, understood, and agreed to this disclaimer in its entirety. If you do not agree with any part of this disclaimer, you must refrain from using the tool.

This disclaimer is subject to change without notice. It is your responsibility to review and understand the most current version of this disclaimer before using the Port Scanner Proof of Concept.

Date: 6-11-2023
