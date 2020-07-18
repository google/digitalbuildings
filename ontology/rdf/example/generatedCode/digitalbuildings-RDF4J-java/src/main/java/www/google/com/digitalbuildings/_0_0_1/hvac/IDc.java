package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_percentage_command;
/**
* Class Dc 
* Tag for dry coolers (sensible, closed-loop coolers).
*/
public interface IDc extends IEquipment{

	public IRI iri();

    public void addUsesOptionalsCooling_percentage_command (ICooling_percentage_command parameter);

	public Set<ICooling_percentage_command> getUsesOptionalsCooling_percentage_command();

}