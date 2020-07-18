package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.IZone;
import www.google.com.digitalbuildings._0_0_1.subfields.IOccupancy;

public interface IZone_occupancy_status_2 extends IField{

	public IRI iri();

    public void addComposedOfOccupancy (IOccupancy parameter);

	public Set<IOccupancy> getComposedOfOccupancy();

    public void addComposedOfStatus (IStatus parameter);

	public Set<IStatus> getComposedOfStatus();

    public void addComposedOfZone (IZone parameter);

	public Set<IZone> getComposedOfZone();

}