package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_use_label;
/**
* Class Vav 
* Tag for terminal units with variable volume control.
*/
public interface IVav extends IEquipment{

	public IRI iri();

    public void addUsesOptionalsZone_use_label (IZone_use_label parameter);

	public Set<IZone_use_label> getUsesOptionalsZone_use_label();

}